# Sites de turismo e reservas

## Sites pesquisados

Foram usados os sites:
    - https://www.tripadvisor.com/
    - https://www.booking.com/
    - https://www.zomato.com/
    - https://www.yelp.com/

### (Im)Possibilidade de uso de APIs

Dos quais em nenhum foi observada uma facilidade na obtenção de acesso às suas APIs, e apenas alguns (3/4) oferecem acesso à documentção da(s) mesma(s) fácilmente. A maioria requer um contacto, que foi tentado e continua sem resposta até hoje (contactos inicidados por G.A.17440, entre dia 26 e 29 de Out, e hoje sendo dia 1 de Nov).

Os que oferecem documentação foi observado que todos subdividem os seus serviços de API em 3 ou 4 APIs para casos de uso especificos (reservas, dados, etc) em vez de uma com endpoints que oferecem solução para todos os casos.

### Necessidade de Web Scraping

Com o acima dito, é necessessário recorrer a soluções de Web Scraping. A comunidade internauta reparou no mesmo, visto que em reação ao observado existem dezenas de projectos e tutoriais de Web Scraping das variadas plataformas de turismo e reservas. Infelizmente, as mesmas não ajudam no processo e cada uma têm um forma de actuação bastante diferente.

## Bibliotecas de Python para Web Scraping

Para fazer Web Scraping vamos usar Python, pela sua facilidade de uso e multifaceta _"Development speed is more important than execution speed"_. Com Python também temos as opções de criar cadernos Jupyter onde o proprio codigo e os resultados são "encadernados" com paragrafos de texto fazendo o proprio projecto o seu pequeno relatorio de preogresso e resultados; como tamém a criação de ambientes virtuais (containers), onde os pacotes usados ficam registados e instaldos localmente, garantindo assim a portabilidade.

Para tal linguagem existem 5 grandes bibliotecas para a resolução deste caso:
    - Requests
    - BeautifulSoup
    - Scrappy
    - lxml
    - Selenium

Cada uma tendo vantagens e desvantagens diferentes, um pequeno exemplo é o Selenium (a mais conhecida), que é a biblioteca mais completa e poderosa das listadas, mas tem um nivel de complxidade maior e requer um setup inicial maior e mais trabalhoso, requer WebDrivers para a execução das tarefas, pode ser "manhosa" com Firefox, sendo preferencial usar Chromium-based Browsers como o Chrome e o novo Edge (necessario ainda o ChromeDriver e o EdgeDriver), visto que esta ferramenta não é apenas de web scraping mas sim de automação de testes.

Tentaremos evitar essa pela sua complexidade e extras desnecessarios às nossas necessidades e custo temporal do setup inicial. Caso seja necessario usar, não vamos hesitar. Para cada website pode ser necessario usar bibliotecas diferentes por necessidade ou por obtenção de informações/blog posts/etc.. que facilitem ou melhorem o output desejado.

### Tratamento do output

Os outputs do conteudo scraped podem vir em .xml ou .csv (ou outras mas essencialmente essas duas). Tentaremos ao maximo usar .csv, e transformar qualquer .xml em .csv, visto que um maior numero de ferramentas graficas (Excel, PowerBI, etc..) e/ou bibliotecas de Python (Pandas, matplotlib, etc) para analise de dados tratam melhor ficheiros separados por virgulas.

Será feita também uma analise e extração de keywords nos textos das decrições e reviews. Para tál existem variados algoritmos que podemos usar, alguns "classicos" outros até de machine learning.

Inicialmente todas as informações (dados e meta-dados) são dados como relevantes, após consideração e poderação durante analises iniciais do decorrer do estudo poderemos descartar dados que não consideremos relevantes. No entanto nada nos impede de tentar prever ou imaginar quais esses serão e posteriormente avaliar o nosso julgamento para ver o que foi aprendido.

#### Informações necessarias (previsão)
Web crawling VS web scraping

Web crawling, também conhecido como Indexação, é usado para indexar as informações na página usando bots também conhecidos como rastreadores. O rastreamento é essencialmente o que os motores de busca fazem. É uma questão de visualizar uma página como um todo e indexá-la. Quando um Bot rastreia um site, ele passa por todas as páginas e todos os links, até a última linha do site, em busca de qualquer informação.

O web scraping, também conhecido como extração de dados da web, é semelhante ao web crawling, pois identifica e localiza os dados de destino das páginas da web. A principal diferença é que, com o web scraping, sabemos o identificador de conjunto de dados exato, por exemplo, uma estrutura de elemento HTML para páginas da web que estão sendo corrigidas, da qual os dados precisam ser extraídos.

Melhores ferramentas para web scraping
1.	Scraping-Bot
2.	Scrapingbee
3.	Import.io
4.	PySpider
5.	Data Stermer

#### Informações a descartar (previsão)
vantagens de web scraping

1.	Mais rápido: Manusear grandes quantidades de dados poderiam levar dias ou semanas a serem processados através do trabalho manual, com o uso do scraping podemos reduzir substancialmente o esforço e aumentar a velocidade de decisão

2.	Confiável e consistente: Ao fazer o trabalho manual é muito fácil de haver erros, por exemplo, erros tipográficos, informações esquecidas ou inserção nas colunas erradas. O uso do web scraping garante consistência e a qualidade dos dados.

3.	Ajuda a reduzir a carga de trabalho.

4.	Menor custo: Uma vez implementado o scraping, o custo total da extração de dados é significativamente reduzido, especialmente quando comparado ao trabalho manual.

5.	Manutenção básica: Fazer o scraping de dados geralmente não requer muita manutenção.

desvantagens de web scraping

1.	Baixa proteção: se os dados na web são protegidos, o uso do scraping também pode se tornar um desafio e aumentar os custos.

2.	Dados estruturados: não vai ser possível fazer scraping a 1000 sites diferentes pois cada site tem uma estrutura completamente diferente.  Será necessário haver alguma estrutura básica que difira em determinadas situações.

## Algoritmos de analise de texto

### Algoritmos Classicos

### Algorimos de machine learning
