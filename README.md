# 📊 Identificador de Não-Seguidores no Instagram

Este script em Python analisa os dados exportados do seu perfil do Instagram e identifica **quais usuários você segue, mas que não te seguem de volta**.

--

## 🧠 Funcionalidade

O programa compara duas listas:

- `following.json`: pessoas que você segue.
- `followers_1.json`: pessoas que te seguem.

Com base nessa comparação, ele gera um arquivo `nao_seguidores.txt` contendo os perfis que você **segue, mas que não te seguem de volta**.

--

## 📥 Como obter seus dados do Instagram

Para usar este script, você precisa baixar seus dados diretamente do Instagram. Siga os passos abaixo:

1. Acesse seu perfil do Instagram (pelo navegador).
2. Vá em **Configurações e privacidade > Suas informações > Baixe suas informações**.
3. Solicite o download completo **desde o início da sua conta**.
4. Escolha o formato **JSON**.
5. Aguarde o e-mail do Instagram com o link para download.
6. Extraia o conteúdo do arquivo `.zip` recebido.
7. Dentro da pasta extraída, navegue até o diretório:

`followers_and_following/`

8. Copie os arquivos abaixo:
- `following.json`
- `followers_1.json`

--

## ▶️ Como executar no Google Colab

1. Acesse [Google Colab](https://colab.research.google.com/).
2. Crie um novo notebook.
3. No primeiro bloco de código, envie os arquivos `following.json` e `followers_1.json` para o ambiente do Colab.
4. Crie uma nova célula no notebook, cole o conteúdo do código main.py e execute.
5. O script irá retornar um arquivo chamado `nao_seguidores.txt` com a relações dos usuários que não te seguem de volta.
