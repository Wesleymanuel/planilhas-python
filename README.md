primeiro importo a biblioteca pandas do python 

logo em seguida crio a variável df que recebe o arquivo Exel 

a função validar verifica se os dados não estão preenchidos de forma errada,
essa validação é feita através de um for que percorre as séries do data frame,
e confere se estão null ou existe atrás do .isna e converte tudo para string, após isso
faz a última verificação com .strip

caso haja erros, o arrey erro sofre adoções 

então ao final, o programa retorna a planilha e os erros que ela contem 
