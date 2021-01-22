import time,gurobipy
import numpy as np
import cvxpy as cp

# Discounted attention scores for different positions in a ranked recommendation
# Only top-k out of n (n<=k) items get non-zero attention scores (as detailed in the paper)
def discounted_attention(k,n):
    A={}
    for i in range(k):
        A[i]=1.0/np.log2(i+2)
    s=sum(A.values())
    for i in A:
        A[i]/=s
    for i in range(k,n):
        A[i]=0
    return A.copy()

# Sample code for the proposed linear programming approach
'''
INPUTS: All the details required for one instance of ranking
    E (array) = current exposure of businesses in an array
    capacity (array) = safe capacities of businesses in an array
    relevances (array) = rele
    k (int) = size of the recommendation
    beta_fraction (float) = beta/beta_max (this ultimately decides how much of exposure we are trying to guarantee for every business)
    lambda_1 (float) = weight (fraction) for the sustainability term in the objective
    lambda_2 (float) = weight (fraction) for the safety term in the objective
    *** lambda_1+lambda_2<=1
OUTPUT: 
    reco = A k-ranked list of businesses
    E = updated exposure of businesses
'''
def LP(E,capacity,relevances,k,beta_fraction,lambda_1,lambda_2):
    # businesses
    businesses=range(len(E))
    
    # total number of businesses
    n=len(businesses)
    
    # beta for minimum exposure
    beta=beta_fraction*1.0/n
    
    # total safe capacity of all the businesses
    s=sum(capacity)+0.0
    
    # normalizing the safe capacity values
    for p in businesses:
        c=capacity[p]/s
        capacity[p]=c
    
    # Attention scores
    A=discounted_attention(k,n)
    
    # Prefiletering size
    N=2*k*k
    
    # matrix to help get final reco (prefil N)
    reco_help=np.zeros((N,1))
    for i in range(N):
        reco_help[i,0]=i

    # Total exposure till now
    E_total=sum(E)
    
    # Sorting businesses in decreasing order of relevances
    sorted_rel=np.argsort(relevances)[::-1][:].tolist()
        
    # Prefiltering businesses
    ### Half prefiltered from top relevant ones
    prefil_businesses=[sorted_rel[i] for i in range(N/2)]
    ### Other half prefiltered from least exposed ones
    sorted_exp=np.argsort(E).tolist()#sorted(E.items(), key=lambda kv: kv[1])
    extra_businesses=[sorted_exp[i] for i in range(N) if sorted_exp[i] not in prefil_businesses]
    prefil_businesses+=extra_businesses[:(N/2)]
    
    # LP variable 
    X=cp.Variable((N,N))

    # LP constraints
    constraints=[]
    # constraint-1: one business gets assigned to one rank only
    constraints.append(cp.sum(X,axis=0)==1)
    # constraint-2: one rank gets only one place
    constraints.append(cp.sum(X,axis=1)==1)
    # constraint-3: all the elements are non-negative
    constraints.append(X>=0)
        
    # cost matrix
    C=np.zeros((N,N))
    # Relevance of top relevant business
    V_max=relevances[sorted_rel[0]]
    #A_mat=np.array([A[i] for i in range(n)]).reshape(n,1)
    for j in range(N):
        for p in range(N):
            #business id
            plc=prefil_businesses[p]
            C[j,p]=(lambda_1*max(0,(beta*(E_total+1.0)-E[plc]-A[j])/(beta*(E_total+1.0))))+(lambda_2*max(0,(E[plc]+A[j]-capacity[plc]*(E_total+1.0))/(capacity[plc]*(E_total+1.0))))+(1-lambda_1-lambda_2)*A[j]*((V_max-relevances[plc])/V_max)
    
    # LP objective
    obj_fn=cp.Minimize(cp.sum(cp.sum(cp.multiply(C,X))))

    # Problem definition and solve
    prob=cp.Problem(obj_fn,constraints)
        
    # =======LP start time=======
    start=time.time()    
    # Solve LP
    prob.solve(solver=cp.GUROBI)    
    # =======LP end time=======
    end=time.time()

    # Result
    Y=X.value
        
    # Indices of businesses in the ranked list
    R=list(np.matmul(Y,reco_help).reshape(N))
        
    # Recommendation : Ranked list of businesses
    reco=[prefil_businesses[int(i)] for i in R[:k]]
        
    # New exposure scores
    for i in range(k):
        E[reco[i]]+=A[i]
    
    print("time taken by LP = "+str(end-start))
    return reco,E