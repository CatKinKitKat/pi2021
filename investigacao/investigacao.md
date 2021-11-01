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

#### Informações a descartar (previsão)

## Algoritmos de analise de texto

### Algoritmos Classicos

### Algorimos de machine learning
