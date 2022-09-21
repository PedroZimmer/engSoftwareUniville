<html>
  <head>
    <title>Formulário</title>
  </head>
  <body>
    <form action="processa.php" method="POST">
        <!-- IMPORTANTE - fieldset e legend não
        são obrigatórios-->
        <fieldset>
            <legend>Dados Pessoais</legend>
            <p>
                <label for="nome">Nome:</label>
                <input type="text" name="txtnome" 
                    id="nome" placeholder="Digite seu nome completo">
                <input type="hidden" name="secreto" value="1234">
            </p>
            <p>
                <label for="email">Email:</label>
                <input type="email" name="txtemail" id="email">
            </p>
            <p>
                <label for="senha">Senha:</label>
                <input type="password" name="txtsenha" id="senha">
            </p>
            <p>
                <label for="data">Data:</label>
                <input type="date" name="txtdata" id="data">
            </p>
            <p>
                <label for="cor">Cor:</label>
                <input type="color" name="txtcor" id="cor">
            </p>
            <p>
                <label for="checkidade">Maior de idade:</label>
                <input type="checkbox" name="cbidade" id="checkidade">
            </p>
            <p>
                <label for="rbcidade">Mora em Joinville:</label>
                <input type="radio" name="rbcidade" id="rbcidade" value="jlle">
                <label for="rbcidade">Mora em Curitiba:</label>
                <input type="radio" name="rbcidade" id="rbcidade" value="cwb">
            </p>
            <p>
                <label for="arquivo">Arquivo:</label>
                <input type="file" name="arquivo" id="arquivo">
            </p>
            <p>
                <label for="selecao">Selecao:</label>
                <select name="selecao" id="selecao">
                    <?php for($i=0;$i<10;$i++){ ?>
                    <option><?=$i ?></option>
                    <?php } ?>
                </select>
            </p>
            <p>
                <label for="textao">Textão:</label>
                <textarea name="textao" id="textao"></textarea>
            </p>
        </fieldset>
        <fieldset>
            <legend>Suas preferências</legend>
        </fieldset>
        <input type="submit">
        <input type="reset" value="limpar">
    </form>
  </body>
</html>