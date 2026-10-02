#!/usr/bin/python3
# \left) and \right) adjust size dynamically

expr = r'\dfrac{\mu}{k_{eff}} \quad \Big( \dfrac{\mu}{k_{eff}} + 1 \Big) \\\\' \
       r'\alpha^{Enz_A}_{rxn_1} \quad \alpha^{Enz_B}_{rxn_2} \quad \Big( \alpha^{Enz_C}_{rxn_2} + 1 \Big) \\\\' \
       r'\left[ \text{TU\ length} \right] \alpha^{RNAP}_{tx} \\\\' \
       r'\alpha^{tRNA+}_{tl} \quad \alpha^{L}_{charging} \Big( 1 + \alpha^{tRNA+}_{tl} \Big) \\\\' \
       r'\Big( \alpha^{mRNA}_{tl} \quad \beta^{mRNA}_{tl} \Big) \quad ' \
       r'\left[ \text{TU\ length} - 1 \right] \alpha^{D}_{tl} \beta^{mRNA}_{tl} \quad ' \
       r'\left[ \text{protein\ length} \right] \alpha^{ribo}_{tl} \\\\' \
       r'\Big[ \quad \Big] \quad \Big( \quad \Big) \quad \left[ \text{TU\ length} \right] \alpha^{D}_{tl} \beta^{mRNA}_{tl} \quad \left[ \text{protein\ length} + 1 \right] \alpha^{ribo}_{tl} \\\\' \
       r'\beta^{Enz_A}_{rxn} \quad \beta^{Enz_B}_{rxn} \quad \beta^{Enz_C}_{rxn} \\\\' \
       r'\beta^{mRNA}_{tl} \quad \beta^{rRNA}_{generic\ formation} \quad \beta^{tRNA}_{tl} \quad \beta^{ncRNA}_{tx} \quad \beta^{tmRNA}_{tx} \\\\' \
       r'\beta^{ribo}_{rxn} \quad \beta^{RNAP}_{rxn} \quad \beta^{D}_{rxn} \quad \beta^{L}_{rxn} \quad \beta^{TU}_{tx} \\\\' \
       r'\alpha^{proteasome}_{rxn} \quad \beta^{proteasome}_{rxn} \quad \alpha^{protease}_{rxn} \quad \beta^{protease}_{rxn} \\\\' \
       r'\sum_{Prot=1}^{N} \quad \sum_{AA=1}^{\text{prot\ length}} \quad \sum_{nt=1}^{\text{TU\ length}} \quad ' \
       r'\textstyle\sum_{Prot=1}^{N} \quad \textstyle\sum_{AA=1}^{\text{prot\ length}} \quad \textstyle\sum_{nt=1}^{\text{TU\ length}} \\\\' \
       r'\sum_{j}^{} \alpha^{X_{j}}_{tx} \quad \sum_{j}^{} \alpha^{X_{j}}_{tl} \quad ' \
       r'\textstyle\sum_{j} \alpha^{X_{j}}_{tx} \quad \textstyle\sum_{j} \alpha^{X_{j}}_{tl} \\\\' \
       r'k_1 \quad k_2 \quad v_1 \quad v_2 \quad v_2 = \dfrac{k_1 v_1}{k_2} \quad c_1 \quad c_2 \quad c_3 \quad c_4 \\\\' \
       r'\Big(c_1 \frac{MW_1}{1000} + c_2 \frac{MW_2}{1000} + c_3 \frac{MW_3}{1000} + c_4 \frac{MW_4}{1000} \Big) \\\\' \
       r'\frac{MW_{P}}{1000} \quad \frac{MW_{R}}{1000} \quad \frac{MW_{C}}{1000} \quad v = \mu c_1 \frac{MW_1}{1000} \\\\' \
       r'ATP + water \quad ADP + P_{i} \quad GAM \quad NGAM \quad H_{2}O \quad \mu GAM + NGAM \\\\' \
       r'\text{LB}=0  \quad \text{UB}=1000 \quad 0 \leq v_{2} \leq 1000 \\\\' \
       r'\max_{\mu,\vec{v}} \quad \vec{c}^{\,T}\vec{v} \qquad \text{subject to} \qquad S\vec{v} = 0 \\\\' \
       r'\max_{\mu} \quad \mu \\ \text{s.t.} \qquad S\vec{v}(\mu)=0,\quad \vec{LB}\leq\vec{v}(\mu)\leq\vec{UB} \\\\' \
       r'\max_{\mu} \quad \mu \\ \text{s.t.} \qquad S(\mu,r_0,\kappa_\tau,\alpha^{met_i}_{rxn_j},\beta^{met_i}_{rxn_j},\vec{k}_{eff},f_{RNA},m_{aa})\vec{v}(\mu)=0 \\ \vec{L}\leq\vec{v}(\mu)\leq\vec{U} \\\\' \
       r'\max_{\mu} \quad \mu \\ \text{s.t.} \quad S(\mu)\vec{v}(\mu)=0 \quad \\ \vec{L}\leq\vec{v}(\mu)\leq\vec{U} \\\\' \
       r'...'

# expr = sympy.latex(expr.replace('beta', 'alpha'))

import sympy
sympy.preview(sympy.Symbol(expr), output='svg', viewer='file', euler = False, packages = ('mathrsfs',),
           filename='coupling_coefficients.svg')

# import matplotlib.pyplot as plt
# fig = plt.figure()
# fig.text(0.05, 0.5, f'{expr}')
# fig.savefig('coupling_coefficients.svg', bbox_inches='tight')
# plt.close(fig)
