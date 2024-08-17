Etapa I - Fundamentos de Teste



1 - Acesse a aplicação indicada:


    O alvo infojobs.com.br trata-se de um site de empregos online.
    Nele buscas de vagas podem ser feitas assim como as empresas podem fazer anuncios de oportunidades.


2 - Identifique e Mapeie os cenários de testes possíveis;:


    Os cenarios de testes possiveis serao identificados e mapeados de acordo com algumas das funcionalidades do site:

        Busca de Vagas: Filtros de busca (localizacao, area de atuacao, tipo de contrato, etc.);
        Cadastro de Usuario: Criar conta, login, recuperacao de senha;
        Cadastrar CV;
        Anunciar vagas;
    
    Com isso diversos cenarios podem ser explorados. Por exemplo:

        Cenario 1: Cadastro com sucesso (dados validos);
        Cenario 2: Cadastro com falha (dados invalidos, e-mail ja cadastrado, etc.) ;
        Cenario 3: Busca por palavra-chave (resultados relevantes);
        Cenario 4: Busca por localizacao (resultados filtrados corretamente);
        Cenario 5: Busca sem resultados (pesquisa com caracteres avulsos);
        Cenario 6: Candidatura com sucesso (curriculo completo);
        Cenario 7: Candidatura com falha (curriculo incompleto).
        

3 - Descreva uma estratégia de testes para a execução:


    Uma estrategia que poderia ser usada seria testes de funcionalidade, Verificar se todas as funcionalidades do site
    funcionam conforme o esperado, incluindo busca de vagas, cadastro de usuario, criacao de curriculo e anuncio de vagas:

        Cadastro de Usuario: Testar fluxos de criacao de conta, login, e recuperacao de senha. Verificar tanto cenarios
        de sucesso quanto falhas (dados invalidos, duplicidade de e-mail, etc).
        Esta sera a funcionalidade a qual o plano de teste sera criado na etapa seguinte, mas outras opcoes poderiam ser:

        Edicao de CV: Testar a funcionalidade de edicao do currículo, incluindo a atualizacao de informacões pessoais,
        formacao acadêmica, experiências profissionais, etc;

        Busca de Vagas: Validar que a busca retorna resultados relevantes, que os filtros (por localizacao, palavra-chave,
        tipo de contrato) funcionam corretamente e que a busca exibe mensagens adequadas quando nao ha resultados;

        Candidatura a Vagas: Assegurar que usuarios com curriculos completos possam se candidatar com sucesso, e que o
        sistema lida apropriadamente com curriculos incompletos;

        Anuncio de Vagas: Verificar o processo de criacao, edicao e exclusao de vagas por empresas. 


4 - Elabore um plano de teste para essa aplicação:


        Funcionalidade: Cadastro de Usuario
            Como um novo usuario
            Quero poder me cadastrar no site
            Para que eu possa acessar as oportunidades de emprego

            Cenario: Cadastro com sucesso
                Dado que estou na pagina inicial do site
                Quando eu seleciono "Login"
                E escolho a opcao para cadastrar-se como "Candidato"
                E preencho o campo "Nome e sobrenome" com "Edgleyson Silva"
                E preencho o campo "E-mail" com "edgleysonsilva99@gmail.com"
                E preencho o campo "Senha" com "SenhaSegura123"
                E preencho o campo "CEP" com "52080-290"
                E preencho o campo "Cargo Desejado" com "QA Analyst"
                E marco o checkbox "Li e aceito as Condicões Legais e a Política de Privacidade"
                E clico no botao "CADASTRAR-SE"
                Entao devo ser redirecionado para a pagina de preenchimento de currículo

            Cenario: Cadastro com falha - dados invalidos na primeira pagina
                Dado que estou na pagina de cadastro de usuario
                Quando preencho algum campo com "" 
                E marco o checkbox "Li e aceito as Condicões Legais e a Política de Privacidade"
                E clico no botao "CADASTRAR-SE"
                Entao devo ver mensagens de erro indicando os campos invalidos

            Cenario: Cadastro com falha - e-mail ja cadastrado
                Dado que existe um usuario cadastrado com o e-mail "usuario@teste.com"
                Quando estou na pagina de cadastro de usuario
                E preencho todos os campos obrigatorios com dados validos
                Mas preencho o campo "E-mail" com "usuario@teste.com"
                Entao devo ver uma mensagem que o e-mail inserido ja esta cadastrado

            Cenario: Cadastro com falha - checkbox de aceite nao marcado
                Dado que estou na pagina de cadastro de usuario
                Quando preencho todos os campos obrigatorios com dados validos
                E nao marco o checkbox "Li e aceito as Condicões Legais e a Política de Privacidade"
                E clico no botao "CADASTRAR-SE"
                Entao devo ver uma mensagem de erro solicitando que aceite os termos e politica de privacidade

            Cenario: Cadastro com falha - senha fraca
                Dado que estou na pagina de cadastro de usuario
                Quando preencho todos os campos obrigatorios com dados validos
                E preencho o campo "Senha" com "123456" 
                E marco o checkbox "Li e aceito as Condicões Legais e a Política de Privacidade"
                E clico no botao "CADASTRAR-SE"
                Entao devo ver uma mensagem de erro informando que a senha é fraca


5 - Identifique eventuais bug:


    Layout e Design:
        Acessando a página de cadastro pelo desktop, existe um banner a esquerda da pagina com a figura de uma mulher com
        descricoes do que o usuario pode esperar que va conseguir com o site e algumas empresas que participam.
        Ao o usuario tentar realizar um cadastro sem o checkbox das condicoes legais e a politica de privacidade aceito, a
        mensagem "Para cadastrar-se é obrigatório ter aceitado as Condições Legais e a Política de Privacidade." é exibida.
        O bug consiste em alem dos campos de cadastros serem reajustado de posicoes devido a exibicao dessa nova mensagem, o 
        banner da esquerda tambem se move em uma especie de zoom que nao e bem necessario pela dimensao da pagina nao mudar tanto.

    Mensagens e Instrucoes:
        Na parte de "Senha", quando uma senha e preenchida com menos de 8 caracteres e exibida a mensagem "Senha inválida. Deve ter
        de 8 a 50 caracteres." Porem, se o usuario digitar uma senha maior que 50 caracteres, a mensagem nao e reexibida. Me parece
        que a senha uma vez que atinge o limite ela fica se sobreescrevendo.


6 - Liste melhorias que forem identificadas:

        Indicador de Forca da Senha: Adicionar um indicador de forca da senha que mostre ao usuario se a senha criada é fraca, média ou
        forte, com dicas para melhora-la.

        Campo de Repetir Senha: Da mais seguranca de que o usuario nao ira cometer um erro digitando a senha duas vezes no cadastro.

        Feedback Visual Claro para Campos Obrigatorios: ornar mais evidente quais campos sao obrigatorios, como adicionar um asterisco (*)
        ao lado dos campos necessarios.

        Opcao de Visualizar Senha: Incluir botao Mostrar/Ocultar

        Confirmacao de Email antes de Finalizar Cadastro: A confirmacao de email é enviada, porem nao ha nenhuma mensagem sobre, o usuario
        é diretamente direcionado ao preenchimento do CV e so ao termino é notificado que é preciso ativar o email.


7 - Forneça parecer sobre a aplicação:


    O site Infojobs.com.br desempenha um papel importante no mercado de trabalho brasileiro, facilitando a conexao entre candidatos e empregadores.
    Após uma análise detalhada, aqui estão os principais pontos observados:

        Experiência do Usuário no Cadastro:

            Indicador de Força da Senha: Adicionar um indicador de força da senha seria uma melhoria significativa, ajudando os usuários a criarem senhas mais seguras.
            Campo de Repetir Senha: Incluir a opção de repetir a senha durante o cadastro aumentaria a segurança e reduziria a chance de erros de digitação.
            Feedback Visual para Campos Obrigatórios: Tornar os campos obrigatórios mais visíveis, com a adição de asteriscos (*), melhoraria a clareza do formulário.

        Opção de Visualizar Senha:

            Inclusão de um botão para visualizar ou ocultar a senha é uma prática comum que aumenta a conveniência e reduz erros durante o preenchimento.

        Confirmacao de E-mail:

            Confirmacao de e-mail ocorre, mas a ausência de uma notificação clara antes do preenchimento do currículo pode confundir o usuário.
            Recomenda-se que a confirmação de e-mail seja destacada antes que o usuário avance para as próximas etapas.


    O Infojobs.com.br é uma ferramenta eficaz para quem busca novas oportunidades de emprego e para empresas que desejam divulgar vagas.
    Porem, alguns ajustes na experiencia do usuario, especialmente no processo de cadastro, poderiam aumentar a segurança e facilitar ainda mais o uso da plataforma.
    Implementar as melhorias sugeridas pode resultar em uma maior satisfacao dos usuários e potencialmente aumentar as taxas de cadastro e retenção na plataforma.

