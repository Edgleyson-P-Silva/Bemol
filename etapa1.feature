1 - O alvo infojobs.com.br trata-se de um site de empregos online.
    Nele busca de vagas podem ser feitas assim como as empresas podem fazer anuncios de oportunidades.


2 - Os cenarios de testes possiveis serao identificados e mapeados de acordo com algumas das funcionalidades do site:

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
        

3 - Uma estrategia que poderia ser usada seria testes de funcionalidade, Verificar se todas as funcionalidades do site
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


4 - Planos de Teste:

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
