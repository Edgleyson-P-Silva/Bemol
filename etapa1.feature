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
        de sucesso quanto falhas (dados invalidos, duplicidade de e-mail);

        Busca de Vagas: Validar que a busca retorna resultados relevantes, que os filtros (por localizacao, palavra-chave,
        tipo de contrato) funcionam corretamente e que a busca exibe mensagens adequadas quando nao ha resultados;

        Candidatura a Vagas: Assegurar que usuarios com curriculos completos possam se candidatar com sucesso, e que o
        sistema lida apropriadamente com curriculos incompletos;

        Anuncio de Vagas: Verificar o processo de criacao, edicao e exclusao de vagas por empresas. 


4 - Planos de Teste:

        Funcionalidade: Cadastro de Usuario
            Cenário: Cadastro com sucesso
                Dado que estou na página de cadastro de usuário
                Quando preencho todos os campos obrigatórios com dados válidos
                E clico no botão "CADASTRAR-SE"
                E sou redirecionado para a página de preenchimento de curriculo
                E preencho todos os campos obrigatórios com dados válidos
                E clico no botão "Minha Area"
                Então sou redirecionado para meu perfil recem criado
        
    



