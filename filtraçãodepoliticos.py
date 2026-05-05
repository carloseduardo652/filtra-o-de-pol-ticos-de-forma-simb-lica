import tkinter as tk
from tkinter import messagebox, scrolledtext

class ProjetoFiltracaoPoliticos:
    def __init__(self, root):
        self.root = root
        self.root.title("projeto de filtração de políticos")
        self.root.geometry("950x800")
        
        # Banco de Dados de Candidatos com status de bloqueio[cite: 7]
        self.candidatos = [
            {
                "id": 1, "nome": "Rafael da silva Cardoso", "cidade": "Belém", "partido": "paz", "senha": "a", "status": "aprovado",
                "detalhes": "Pontuação na prova: 26 acertos e 4 erros\n\nCurrículo geral: Agente público com experiência em gestão governamental, formulação, implementação e avaliação de políticas públicas. Ao longo do mandato, atuou na proposição e execução de projetos estruturantes nas áreas de educação, saúde, infraestrutura e desenvolvimento socioeconômico. Possui domínio de planejamento estratégico, gestão por indicadores e acompanhamento de metas, com foco em eficiência administrativa, otimização de recursos e entrega de resultados mensuráveis. Experiência em articulação institucional, elaboração normativa e fiscalização da aplicação de recursos públicos.\n\nQual é o seu diferencial: Atuação orientada por evidências e indicadores de desempenho, com histórico de projetos implementados e monitorados por métricas claras. Capacidade de integrar planejamento técnico com viabilidade política, assegurando execução efetiva das propostas. Experiência na estruturação de programas com foco em custo-benefício, transparência e accountability. Perfil analítico, com ênfase em tomada de decisão baseada em dados, avaliação de impacto e melhoria contínua de políticas públicas.\n\nO que você pretende fazer na política: Dar continuidade e escalar programas com resultados comprovados, ampliando sua cobertura e eficiência. Implementar novos projetos com base em diagnóstico técnico e análise de dados, priorizando áreas estratégicas como educação, saúde, infraestrutura e geração de emprego e renda. Aperfeiçoar mecanismos de governança, transparência e controle, com fortalecimento de sistemas de monitoramento e avaliação. Consolidar uma gestão pública orientada a resultados, com metas claras, indicadores de desempenho e prestação de contas sistemática à sociedade."
            },
            {
                "id": 2, "nome": "Maria da costa Bahia", "cidade": "campinas", "partido": "muito", "senha": "b", "status": "aprovado",
                "detalhes": "Pontuação da prova: 28 acertos e 2 erros\n\nCurrículo geral: Gestora pública com experiência na elaboração, tramitação e aprovação de projetos legislativos e programas governamentais de impacto estrutural. Durante o mandato, foi responsável pela proposição de iniciativas convertidas em normas e políticas públicas nas áreas de gestão fiscal, educação, saúde e infraestrutura. Possui domínio dos instrumentos de planejamento governamental (PPA, LDO e LOA), análise orçamentária e conformidade com a Lei de Responsabilidade Fiscal. Atua com acompanhamento sistemático da execução financeira e avaliação de políticas públicas com base em indicadores de desempenho. Experiência em articulação interinstitucional e fiscalização da aplicação de recursos públicos.\n\nQual é o seu diferencial: Histórico consistente de projetos aprovados e implementados, com foco em eficiência, impacto mensurável e sustentabilidade fiscal. Capacidade de estruturar propostas tecnicamente robustas, alinhadas à viabilidade orçamentária e aos marcos regulatórios vigentes. Atuação baseada em princípios de governança, transparência e accountability, com uso de métricas e auditorias para monitoramento contínuo. Perfil técnico, analítico e orientado a resultados, com ênfase na melhoria da qualidade do gasto público e na entrega de benefícios concretos à população.\n\nO que você pretende fazer na política: Ampliar e consolidar políticas públicas já aprovadas, garantindo maior escala, eficiência e cobertura. Desenvolver novos projetos com base em evidências, diagnóstico técnico e análise de dados, priorizando áreas estratégicas como educação, saúde, infraestrutura e geração de renda. Fortalecer mecanismos de governança, controle e transparência, com integração de soluções digitais para monitoramento e prestação de contas. Manter uma atuação orientada a resultados, com metas claras, indicadores de desempenho e avaliação contínua do impacto das políticas implementadas."
            },
            {"id": 3, "nome": "Vazio ainda", "cidade": "", "partido": "", "senha": "c", "status": "vazio", "detalhes": ""},
            {"id": 4, "nome": "Vazio ainda", "cidade": "", "partido": "", "senha": "d", "status": "vazio", "detalhes": ""},
            {"id": 5, "nome": "Vazio ainda", "cidade": "", "partido": "", "senha": "e", "status": "vazio", "detalhes": ""},
            {"id": 6, "nome": "Vazio ainda", "cidade": "", "partido": "", "senha": "f", "status": "vazio", "detalhes": ""}
        ]
        
        self.gabarito = {
            1:'C', 2:'D', 3:'E', 4:'B', 5:'A', 6:'D', 7:'D', 8:'C', 9:'E', 10:'A',
            11:'B', 12:'E', 13:'C', 14:'D', 15:'A', 16:'B', 17:'C', 18:'E', 19:'D', 20:'A',
            21:'B', 22:'C', 23:'E', 24:'A', 25:'B', 26:'D', 27:'A', 28:'C', 29:'D', 30:'B'
        }
        
        self.questoes_data = [
            ("1. A corrupção no setor público pode ser definida como:", ["A) Uso eficiente de recursos públicos", "B) Crescimento econômico acelerado", "C) Uso ilegal do poder para benefício próprio", "D) Aplicação de leis rígidas", "E) Fiscalização governamental"]),
            ("2. Um dos principais efeitos da corrupção é:", ["A) Aumento da transparência", "B) Redução da desigualdade", "C) Melhoria dos serviços públicos", "D) Desperdício de recursos públicos", "E) Aumento da confiança nas instituições"]),
            ("3. A falta de transparência contribui para a corrupção porque:", ["A) Aumenta o controle social", "B) Facilita auditorias", "C) Melhora a gestão pública", "D) Reduz os custos públicos", "E) Dificulta a fiscalização"]),
            ("4. Qual ferramenta ajuda no combate à corrupção?", ["A) Sigilo total dos gastos", "B) Portais de transparência", "C) Redução de impostos", "D) Privatização total", "E) Aumento de salários públicos"]),
            ("5. Em países com alta corrupção, geralmente ocorre:", ["A) Pior qualidade dos serviços públicos", "B) Melhor distribuição de renda", "C) Aumento da confiança institucional", "D) Crescimento sustentável", "E) Maior desenvolvimento social"]),
            ("6. A corrupção estrutural está relacionada principalmente a:", ["A) Falhas individuais isoladas", "B) Excesso de tecnologia", "C) Educação de qualidade", "D) Problemas sistêmicos nas instituições", "E) Baixa população"]),
            ("7. Inflação é:", ["A) Redução geral de preços", "B) Crescimento do PIB", "C) Redução da produção", "D) Aumento generalizado dos preços", "E) Aumento do emprego"]),
            ("8. Crescimento econômico refere-se a:", ["A) Melhoria na qualidade de vida", "B) Redução da pobreza", "C) Aumento da produção de bens e serviços", "D) Aumento da educação", "E) Igualdade social"]),
            ("9. O desemprego elevado tende a:", ["A) Aumentar o consumo", "B) Melhorar salários", "C) Aumentar investimentos", "D) Reduzir pobreza", "E) Reduzir a economia"]),
            ("10. Política monetária envolve:", ["A) Controle da moeda e juros", "B) Educação pública", "C) Política ambiental", "D) Legislação trabalhista", "E) Gastos públicos"]),
            ("11. A desigualdade de renda pode:", ["A) Aumentar o crescimento sustentável", "B) Prejudicar o desenvolvimento econômico", "C) Eliminar a pobreza", "D) Melhorar a distribuição", "E) Não ter impacto"]),
            ("12. O papel do Estado na economia inclui:", ["A) Não interferir nunca", "B) Apenas arrecadar impostos", "C) Controlar todas empresas", "D) Eliminar o setor privado", "E) Regular e corrigir falhas de mercado"]),
            ("13. Desigualdade social é:", ["A) Igualdade econômica", "B) Crescimento econômico", "C) Diferença de acesso a recursos e oportunidades", "D) Aumento do PIB", "E) Redução da pobreza"]),
            ("14. Um fator histórico da desigualdade é:", ["A) Tecnologia moderna", "B) Internet", "C) Globalização recente", "D) Colonização e escravidão", "E) Industrialização atual"]),
            ("15. A desigualdade impacta principalmente:", ["A) Acesso a oportunidades", "B) Apenas governo", "C) Exportações", "D) Tecnologia", "E) Apenas ricos"]),
            ("16. Programas sociais:", ["A) Nunca funcionam", "B) Podem reduzir desigualdade, mas não resolvem tudo", "C) Eliminar totalmente a pobreza", "D) Aumentam desigualdade", "E) Não têm impacto"]),
            ("17. A educação é importante porque:", ["A) Não impacta economia", "B) Reduz tecnologia", "C) Promove desenvolvimento social e econômico", "D) Aumenta desigualdade", "E) Não influencia trabalho"]),
            ("18. Um desafio da educação pública é:", ["A) Excesso de recursos", "B) Excesso de professores", "C) Alta qualidade geral", "D) Poucos alunos", "E) Falta de infraestrutura"]),
            ("19. A qualidade da educação influencia:", ["A) Apenas cultura", "B) Clima", "C) Agricultura", "D) Mercado de trabalho", "E) Transporte"]),
            ("20. A tecnologia na educação:", ["A) Pode melhorar o aprendizado", "B) Não tem efeito", "C) Substitui professores totalmente", "D) Elimina escolas", "E) Sempre prejudica"]),
            ("21. Um sistema de saúde eficiente:", ["A) Atende poucos", "B) Oferece acesso universal e qualidade", "C) É caro e limitado", "D) Atende só emergências", "E) Não previne doenças"]),
            ("22. Um desafio da saúde pública é:", ["A) Excesso de recursos", "B) Poucos pacientes", "C) Falta de investimento", "D) Baixa demanda", "E) Tecnologia demais"]),
            ("23. Saneamento básico inclui:", ["A) Apenas hospitais", "B) Transporte público", "C) Escolas", "D) Energia elétrica", "E) Água tratada e esgoto"]),
            ("24. Falta de saneamento causa:", ["A) Doenças", "B) Crescimento econômico", "C) Educação melhor", "D) Menos poluição", "E) Melhora da saúde"]),
            ("25. A degradação ambiental é causada por:", ["A) Sustentabilidade", "B) Poluição e desmatamento", "C) Tecnologia limpa", "D) Energia renovável", "E) Educação"]),
            ("26. Desenvolvimento sustentável busca:", ["A) Crescimento sem limites", "B) Apenas lucro", "C) Exploração total", "D) Equilíbrio entre economia e meio ambiente", "E) Redução da produção"]),
            ("27. Preconceito é:", ["A) Julgamento prévio sem base", "B) Educação formal", "C) Política pública", "D) Conhecimento científico", "E) Desenvolvimento social"]),
            ("28. Combater o preconceito exige:", ["A) Ignorar o problema", "B) Aumentar desigualdade", "C) Educação e conscientização", "D) Reduzir diálogo", "E) Evitar diversidade"]),
            ("29. Uma causa da violência urbana é:", ["A) Igualdade social", "B) Educação de qualidade", "C) Emprego alto", "D) Desigualdade e falta de oportunidades", "E) Estabilidade econômica"]),
            ("30. Para reduzir a violência, é importante:", ["A) Ignorar políticas públicas", "B) Investir em educação e inclusão", "C) Aumentar desigualdade", "D) Reduzir policiamento", "E) Eliminar leis"])
        ]

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)
        self.mostrar_pagina_1()

    def limpar(self):
        for w in self.container.winfo_children(): w.destroy()

    def mostrar_pagina_1(self):
        self.limpar()
        tk.Label(self.container, text="projeto de filtração de políticos", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Textos atualizados e sem repetição conforme solicitado[cite: 7]
        textos = [
            "esse projeto tem finalidade de filtrar os possíveis níveis de capacidade de cada político através de um certificado simbólico que Server apenas para influenciar de eleitores de forma coerente, ou seja, retirar políticos sem preparo ou mal intencionados, deixando em evidência no sistema apenas os nomes dos candidatos aprovados com certificado de filtração obtidas por meio de uma prova, proporcionando efeitos de projetos dos políticos mais eficiente e ausência de projetos de políticos mais atrasado.",
            "para conseguir o certificado de filtração é necessário seguir essas atividades de prova: 1. Provas que contem 30 questões de múltipla escolha em diversas áreas, mas modelo aqui é inicial de 30 questões podendo ser ampliado para mais questões e dificuldades aqui é apenas modelo inicial podem ser mais intensas. 2. Currículo geral. 3. Qual é o seu diferencial. 4. o que pretende fazer na política.",
            "os níveis de dificuldades podem ser aumentadas para candidatos políticos que querem certificado de filtração, com objetivo de deixa mais eficiente o beneficio desse projeto. No momento esse programa é apenas um modelo inicial.",
            "Exemplos do modelo inicial sobre senhas que vai aparace aqui, mas se for trabalho para amplia deve oculta as senhas somente permitindo acesso para pessoas corretas: primeiro candidato ”a” próximo candidato”b” próximo ”c”....."
        ]
        
        for t in textos:
            tk.Label(self.container, text=t, wraplength=850, justify="center", pady=8).pack()
        
        tk.Button(self.container, text="avançar como cidadão", command=self.pagina_cidadao).pack(pady=2)
        tk.Button(self.container, text="avançar candidato", command=self.login_candidato).pack(pady=2)
        tk.Button(self.container, text="avançar para validação de quem sou", command=self.pagina_validacao).pack(pady=2)

    def pagina_cidadao(self):
        self.limpar()
        tk.Label(self.container, text="Lista de Candidatos Aprovados", font=("Arial", 12, "bold")).pack(pady=10)
        
        f_busca = tk.Frame(self.container); f_busca.pack()
        tk.Label(f_busca, text="Procurar nome:").pack(side="left")
        e_busca = tk.Entry(f_busca); e_busca.pack(side="left", padx=5)
        
        def buscar():
            nome = e_busca.get().lower()
            for c in self.candidatos:
                if nome in c['nome'].lower() and c['status'] == 'aprovado':
                    messagebox.showinfo("Busca", f"candidato com certificado simbólico de filtração. Está no número {c['id']}")
                    return
            messagebox.showwarning("Busca", "candidato sem certificado simbólico")
        tk.Button(f_busca, text="Buscar", command=buscar).pack(side="left")

        for c in self.candidatos:
            if c['status'] == "aprovado":
                tk.Button(self.container, text=f"{c['id']}. Nome: {c['nome']} / cidade: {c['cidade']} / partido: {c['partido']}", 
                          command=lambda info=c['detalhes']: self.mostrar_detalhes(info)).pack(fill="x", padx=100)
            else:
                tk.Label(self.container, text=f"{c['id']}. Vazio ainda", fg="gray").pack()
        
        tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_1).pack(pady=20)

    def mostrar_detalhes(self, info):
        top = tk.Toplevel(self.root)
        top.title("Informações do Candidato")
        txt = scrolledtext.ScrolledText(top, width=80, height=25)
        txt.insert(tk.INSERT, info)
        txt.config(state=tk.DISABLED)
        txt.pack(padx=10, pady=10)

    def login_candidato(self):
        self.limpar()
        tk.Label(self.container, text="área do candidato", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.container, text="Senha de acesso:").pack(); e_s = tk.Entry(self.container, show="*"); e_s.pack()
        tk.Label(self.container, text="Nome do candidato:").pack(); e_n = tk.Entry(self.container); e_n.pack()
        tk.Label(self.container, text="Cidade:").pack(); e_c = tk.Entry(self.container); e_c.pack()
        tk.Label(self.container, text="Partido:").pack(); e_p = tk.Entry(self.container); e_p.pack()

        def verificar():
            for c in self.candidatos:
                if c['senha'] == e_s.get():
                    if c['status'] == "aprovado":
                        messagebox.showwarning("Bloqueio", "Esta vaga já foi preenchida e não pode mais ser alterada.")
                        return
                    self.fazer_prova(c, e_n.get(), e_c.get(), e_p.get())
                    return
            messagebox.showerror("Erro", "Senha não encontrada.")
        
        tk.Button(self.container, text="teste de filtração", command=verificar).pack(pady=5)
        tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_1).pack(pady=5)

    def fazer_prova(self, obj, nome, cid, part):
        self.limpar()
        canvas = tk.Canvas(self.container)
        scroll = tk.Scrollbar(self.container, orient="vertical", command=canvas.yview)
        f_questoes = tk.Frame(canvas)
        f_questoes.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0,0), window=f_questoes, anchor="nw")
        canvas.configure(yscrollcommand=scroll.set)
        
        respostas = []
        for i, (pergunta, alternativas) in enumerate(self.questoes_data):
            tk.Label(f_questoes, text=pergunta, font=("Arial", 10, "bold"), wraplength=800, justify="left").pack(anchor="w", pady=(10,0))
            v = tk.StringVar(value="X")
            respostas.append(v)
            for alt in alternativas:
                tk.Radiobutton(f_questoes, text=alt, variable=v, value=alt[0]).pack(anchor="w", padx=20)

        canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        # Botão de finalizar criado dentro do container da prova para evitar duplicação[cite: 7]
        btn_finalizar = tk.Button(self.container, text="Finalizar Prova", bg="green", fg="white", 
                                  command=lambda: self.finalizar_prova_logica(respostas, obj, nome, cid, part))
        btn_finalizar.pack(pady=10)

    def finalizar_prova_logica(self, respostas, obj, nome, cid, part):
        acertos = sum(1 for i, v in enumerate(respostas) if v.get() == self.gabarito[i+1])
        messagebox.showinfo("Resultado", f"Acertos: {acertos} | Erros: {30-acertos}")
        if acertos >= 20:
            self.fase_subjetiva(obj, nome, cid, part, acertos)
        else:
            messagebox.showerror("Reprovado", "Menos de 20 acertos."); self.mostrar_pagina_1()

    def fase_subjetiva(self, obj, nome, cid, part, acertos):
        self.limpar()
        tk.Label(self.container, text="Currículo Geral (300 a 1000 caracteres):").pack()
        t1 = scrolledtext.ScrolledText(self.container, height=6); t1.pack()
        tk.Label(self.container, text="Qual é o seu diferencial:").pack(); t2 = scrolledtext.ScrolledText(self.container, height=6); t2.pack()
        tk.Label(self.container, text="O que você pretende fazer na política:").pack(); t3 = scrolledtext.ScrolledText(self.container, height=6); t3.pack()

        def salvar():
            info = f"Pontuação: {acertos} acertos e {30-acertos} erros\n\nCurrículo: {t1.get('1.0','end')}\nDiferencial: {t2.get('1.0','end')}\nProjeto: {t3.get('1.0','end')}"
            obj.update({"nome": nome, "cidade": cid, "partido": part, "status": "aprovado", "detalhes": info})
            messagebox.showinfo("Sucesso", "Candidato Registrado!"); self.mostrar_pagina_1()

        tk.Button(self.container, text="Enviar para Avaliação", command=salvar).pack(pady=10)

    def pagina_validacao(self):
        self.limpar()
        novo_texto = "para obter senha de acesso como candidato politico é preciso se identifica pela vídeo chamada do numero pelo numero de celular 2837663773 para apresente documentos que valida de fato quem você se apresentou"
        tk.Label(self.container, text=novo_texto, font=("Arial", 12), wraplength=800, justify="center").pack(pady=50)
        tk.Button(self.container, text="Voltar", command=self.mostrar_pagina_1).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ProjetoFiltracaoPoliticos(root)
    root.mainloop()