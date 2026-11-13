import numpy as np, json
X=np.array([[400,22,20,22],[230,12,5,8],[500,7,3.5,5],[1200,22,12,22],[900,22,10,22],[200,22,.6,22],[350,4,1,4],[70,6,30,5],[600,3,6,1],[1300,10,15,12]],dtype=float)
benefit=np.array([True,True,True,False])
R=(X-X.min(0))/(X.max(0)-X.min(0)); R[:,~benefit]=1-R[:,~benefit]
cor=np.corrcoef(R,rowvar=False)
sd=R.std(0,ddof=0); info=sd*(1-cor).sum(0); critic=info/info.sum()
def rank(v):
    return [int(1+np.sum(v>x+1e-12)) for x in v]
def result(w):
    V=X/np.sqrt((X*X).sum(0))*w
    best=np.where(benefit,V.max(0),V.min(0)); worst=np.where(benefit,V.min(0),V.max(0))
    dp=np.linalg.norm(V-best,axis=1); dm=np.linalg.norm(V-worst,axis=1)
    top=dm/(dp+dm)
    P=(R[:,None,:]>R[None,:,:]).astype(float)@w
    pos=P.sum(1)/9; neg=P.sum(0)/9; net=pos-neg
    return dict(weights=w.tolist(),saw=(R@w).tolist(),saw_rank=rank(R@w),
        topsis=top.tolist(),topsis_rank=rank(top),topsis_positive_distance=dp.tolist(),topsis_negative_distance=dm.tolist(),
        promethee_usual_positive=pos.tolist(),promethee_usual_negative=neg.tolist(),promethee_usual_net=net.tolist(),promethee_rank=rank(net))
def smaa(seed=20261106,N=1000000,ordered=False):
    rng=np.random.default_rng(seed); b=np.zeros((10,10)); totals=np.zeros((10,4))
    for start in range(0,N,10000):
        W=rng.dirichlet(np.ones(4),size=min(10000,N-start))
        if ordered:
            sorted_weights=np.sort(W,axis=1)[:,::-1]
            W=sorted_weights[:,[0,2,1,3]]
        score=W@R.T; order=np.argsort(-score,axis=1,kind='stable')
        for r in range(10): b[:,r]+=np.bincount(order[:,r],minlength=10)
        for i in range(10): totals[i]+=W[order[:,0]==i].sum(0)
    first=b[:,0].copy()
    central=[(totals[i]/first[i]).tolist() if first[i] else None for i in range(10)]
    b/=N
    return dict(seed=seed,samples=N,generator='NumPy default_rng PCG64',distribution='Dirichlet(1,1,1,1)'+(' ordered w1 >= w3 >= w2 >= w4' if ordered else ''),rank_acceptability=b.tolist(),mean_rank=(b@np.arange(1,11)).tolist(),central_weights=central,first_place_standard_error=np.sqrt(b[:,0]*(1-b[:,0])/N).tolist())
out=dict(status='Exploratory, monetary units confirmed; pending period, definitions, preference and AHP confirmation',labels=[f'L{i+1:02}' for i in range(10)],source='Imagem fornecida por Lucas em 2026-11-06; 40 valores conferidos visualmente de forma independente',raw_values=X.tolist(),benefit_assumption=benefit.tolist(),minmax_oriented=R.tolist(),correlation_raw=np.corrcoef(X,rowvar=False).tolist(),correlation_oriented=cor.tolist(),critic_std_population=sd.tolist(),critic_information=info.tolist(),equal=result(np.full(4,.25)),critic=result(critic),smaa_global=smaa(),smaa_ordered=smaa(ordered=True))
out['pareto_dominance']=[[i+1,j+1] for i in range(10) for j in range(10) if i!=j and np.all(R[i]>=R[j]) and np.any(R[i]>R[j])]
out['units']=['R$ milhões','quantidade','R$ milhões/aplicação','quantidade']
out['unit_confirmation']='Lucas confirmou ambas as colunas monetárias em milhões de reais em 2026-11-06'
out['numpy_version']=np.__version__
out['zero_frequency_note']='Frequência zero significa não observado na amostra, salvo prova analítica separada. Erro Monte Carlo não mede incerteza dos dados ou das hipóteses.'
A=np.array([[1,7,5,9],[1/7,1,1/6,3],[1/5,6,1,6],[1/9,1/3,1/6,1]],dtype=float)
eval,evec=np.linalg.eig(A); k=np.argmax(eval.real)
lam=float(eval[k].real); w=evec[:,k].real; w/=w.sum()
out['ahp']=dict(pairwise_matrix=A.tolist(),weights=w.tolist(),lambda_max=lam,CI=(lam-4)/3,RI=0.9,CR=(lam-4)/2.7,threshold=0.10,consistent=bool((lam-4)/2.7<=.10),method='Principal right eigenvector; no judgments changed',judgments_source='Leopoldo, WhatsApp Trabalho Metodos, 11/11/2026 22:42; transcription by visual inspection')
out['ahp_results']=result(w)
out['status']='AHP calculated but CR > 0.10; conditional academic conclusions, not validated operational decision'
out['units']=['R$ milhões','dias com aplicações no mês','R$ milhões/aplicação (denominador a confirmar)','dias com resgates no mês']
out['context']=dict(custody_reference='Início de agosto; ano não informado',operation_period='Mês completo de agosto; ano não informado',source='Fonte interna da companhia, segundo Leopoldo; sistema e extração não identificados',selection='Casos com grande impacto nos números da companhia no mês',decision_maker='Banqueiro responsável pelas contas, segundo Leopoldo',objective='Ordenar atendimento diário das demandas',directions='C1,C2,C3 maximizar; C4 minimizar, confirmados por Leopoldo',permission='Autorização institucional para uso acadêmico não documentada',frequency='22 representa dias de aplicação/resgate no mês, não contagem de operações',pending='Ano, data de extração, sistema, definição/denominador de C3, autoria dos julgamentos, restrições práticas, função de preferência usual e autorização acadêmica')
out['numpy_version']=np.__version__
B=A.copy(); B[1,2]=1/4; B[2,1]=4
be,bv=np.linalg.eig(B); k=np.argmax(be.real); bl=float(be[k].real); bw=bv[:,k].real; bw/=bw.sum()
out['suggested_ahp']=dict(pairwise_matrix=B.tolist(),weights=bw.tolist(),lambda_max=bl,CI=(bl-4)/3,RI=0.9,CR=(bl-4)/2.7,threshold=0.10,consistent=bool((bl-4)/2.7<=.10),status='Technical suggestion requested by Lucas, awaiting decision-maker validation',change='C3/C2: 6 to 4, reciprocal C2/C3: 1/6 to 1/4; other five pairs unchanged',method='Principal right eigenvector')
out['suggested_results']=result(bw)
candidates=[]
scale=[1/i for i in range(9,1,-1)]+list(range(1,10))
for i in range(4):
    for j in range(i+1,4):
        for value in scale:
            M=A.copy(); M[i,j]=value; M[j,i]=1/value
            cr=(float(max(np.linalg.eigvals(M).real))-4)/2.7
            if cr<=0.10:
                candidates.append(dict(i=i+1,j=j+1,original=float(A[i,j]),suggested=float(value),CR=cr,log_distance=float(abs(np.log(value/A[i,j])))))
out['single_pair_candidates']=sorted(candidates,key=lambda q:q['log_distance'])
out['status']='Original AHP inconsistent; suggested single-pair revision passes CR<=0.10 but awaits decision-maker validation; academic analysis only'
out['status']='Analise academica; AHP ajustado com C3/C2=4, confirmado pelo grupo; dados e hipoteses limitados conforme relatorio.'
out['units']=['R$ milhoes','dias com aplicacoes no mes','R$ milhoes (media informada; denominador nao documentado)','dias com resgates no mes']
out['suggested_ahp']['status']='Ajuste confirmado pelo grupo; cenario principal'
out['context']['pending']='Ano, data de extracao, sistema, definicao/denominador de C3, restricoes praticas, funcao usual e autorizacao academica'
# Os nomes suggested_ahp/suggested_results sao conservados para compatibilidade.
out['units'][2]='R$ milhões (média dos valores de aplicações/resgates no mês)'
out['context']['custody_reference']='01/08/2026'
out['context']['operation_period']='01/08/2026–31/08/2026, conforme esclarecimento de Leopoldo'
out['context']['C3_definition']='Média de todos os valores de aplicação/resgates dentro de um mês, segundo Leopoldo. Agregados preservados; não recalculados com transações. Não se presume convenção de sinais ou tratamento dos movimentos.'
out['context']['pending']='Data de extração, sistema, auditoria da agregação com microdados, restrições práticas, função usual e autorização acadêmica'
print(json.dumps(out,ensure_ascii=False,indent=2))

