% Latex style for final reports and dissertations (Instituto Politécnico de Beja)
% Version 0.8.1, 2021/10/01
% Author: João Paulo Barros, joao.barros@ipbeja.pt
% Com contribuições de Henrique Água-Doce, Nuno Mourinho e Raul Carvalho.

% Document adjustment
\LoadClass[11pt,a4paper]{memoir}
\RequirePackage[top=4cm, bottom=3cm, left=3.5cm, right=2.5cm]{geometry} 
\RequirePackage[utf8]{inputenc}
\RequirePackage{ifthen}
\RequirePackage[T1]{fontenc}
\RequirePackage[table]{xcolor}
\RequirePackage{float}

\DeclareOption{PT}{\newcommand{\PT}{PT}}

\ProcessOptions

\DeclareRobustCommand{\pt-en}[2]{%
         \ifthenelse{\isundefined{\PT}}
		{#2} % then 
		{#1} % else
}

\usepackage{csquotes}
\usepackage{longtable}


\pt-en{\RequirePackage[portuges]{babel} }
{\RequirePackage[english]{babel}}
%hifens de quebra de linha ‡ portuguesa
\defineshorthand{"-}{\nobreak\hskip0pt\discretionary{-}{-}{-}\nobreak\hskip0pt}

\usepackage{url}

%\usepackage{xurl}
%https://www.overleaf.com/learn/latex/biblatex_citation_styles
%https://ctan.org/pkg/biblatex-apa?lang=en
\usepackage[
backref=true,
backend=biber,
%style=apa,
style=alphabetic,
%citestyle=alphabetic
]{biblatex}

\pt-en{
\DefineBibliographyStrings{portuges}{%
  backrefpage = {citado na página},% originally "cited on page"
  backrefpages = {citado nas páginas},% originally "cited on pages"
}
}{}

\addbibresource{03-bibliography.bib}

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipbeja-format} [
2013/04/18, 2013/10/10, 2014/07/03, 2020/10/14, 2020/11/02, 2020/11/20, version 0.6, author: João Paulo Barros (joao.barros@ipbeja.pt)
Style for IPBeja Academic work (presently, only in portuguese)
Changes compared to version 0.3:
Layout da capa
Tamanho da fonte 11pt
Outros pormenores mínimos não registados ;-|
]

% graphics, symbols and hyperlink packages
\RequirePackage{graphicx}
\RequirePackage{amssymb}
\RequirePackage{lipsum}
\RequirePackage{listings}
\RequirePackage{datetime}

% Paragraph ajustement
%\setlength{\parindent}{0mm}
%\setlength{\parskip}{3mm}
\renewcommand{\baselinestretch}{1.2} % 1.5 for double-space

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{memoir}}
\ProcessOptions

% Capa e folha de rosto
\DeclareRobustCommand{\folhacapa}{
	\thispagestyle{empty}
	\newpage
	%\noindent{\includegraphics[width=2.85cm]{logos/logo-ipbeja} 
	%\hfill 
	\vspace*{-1cm}	
    \parbox[c]{0.65\textwidth}{
        \begin{center}
    	\includegraphics[width=9cm]{logos/logo-ipbeja} \\
	    	%\vspace*{1cm}
        \end{center}
    }
	\begin{center}
		{{\footnotesize \textbf \ESCOLA}}\\
		\vspace*{.1cm}
		{{\footnotesize \textbf \CURSO}}\\
		\vspace{1.0cm}
		{\LARGE\textbf \TITULO}\\
		\vspace{.5cm}
		{\large\textbf \SUBTITULO}\\
		\vspace{1.5cm}
		{\Large\textit \NOMEALUNO}\\
		\vfill
		\pt-en{\LOCAL, \small \the\day\ de \monthname\ de \the\year}
		      {\LOCAL, \small \the\day\ \monthname\ \the\year}
	\end{center}
	\newpage\hspace{1mm}
}

\DeclareRobustCommand{\folharosto}{
	\thispagestyle{empty}
	\newpage
	\thispagestyle{empty}
	\begin{center}
		\vspace*{0.2cm}
		{{\footnotesize\textbf{INSTITUTO POLITÉCNICO DE BEJA}}}\\
	    \vspace*{.1cm}
		{{\footnotesize\textbf {\ESCOLA}}}\\
		\vspace*{.1cm}
		{{\footnotesize\textbf{{\CURSO}}}}\\
		\vspace{1cm}
		{\LARGE\textbf \TITULO}\\
		\vspace{.5cm}
		{\large\textbf \SUBTITULO}\\
		\vspace{1.0cm}
		{\normalsize \NOMEALUNO}\\
		\vspace{2cm}
		\pt-en{Orientado por}{Advisor}:\\
		\vspace{.2cm}
		\ifthenelse{\isundefined{\ORIENTADORENTIDADE}}
		{} % then vazio
		{%orientador estágio
			\vspace{.2cm}
			\ORIENTADORENTIDADE\\
		}
		%um orientador do curso
		\ORIENTADORIPBEJAA, IPBeja\\
        \ifthenelse{\isundefined{\ORIENTADORIPBEJAB}}
		{} % then vazio
		{% mais um orientador do curso
			\vspace{.2cm}
			\ORIENTADORIPBEJAB, IPBeja\\
		}
		\vspace{2cm}
		\ifthenelse{\isundefined{\DECLARACAO}}
		{} %then vazio
		{\DECLARACAO} 
		\vfill
		\small \the\year
	\end{center}
	\thispagestyle{empty}
	\cleardoublepage
         \pagestyle{ruled}
}

\DeclareRobustCommand{\paginadedicatoria}{
	\@blankoddpage
	\thispagestyle{empty}
	\begin{flushright}
	\ \\
	\vspace{5cm}
	\textit \DEDICATORIA
	\end{flushright}
	\@blankoddpage
}

% Tables of contents, figues and tables

\newcommand{\indicegeral}{
\cleardoublepage
\tableofcontents
}

\newcommand{\indicedefiguras}{
\cleardoublepage
\listoffigures
}

\newcommand{\indicedetabelas}{
\cleardoublepage
\listoftables
}

\newcommand{\indicedelistagens}{
\cleardoublepage
\lstlistoflistings
}

\pt-en{
\addto\captionsportuges{%
  \renewcommand{\lstlistlistingname}%
    {\'{I}ndice de Listagens}%
}

\addto\captionsportuges{%
  \renewcommand{\lstlistingname}%
    {Listagem}%
}

\addto\captionsportuges{%
  \renewcommand{\contentsname}%
    {\'{I}ndice}%
}

\addto\captionsportuges{%
  \renewcommand{\listfigurename}%
    {\'{I}ndice de Figuras}%
}

\addto\captionsportuges{%
  \renewcommand{\listtablename}%
    {\'{I}ndice de Tabelas}%
}

\addto\captionsportuges{%
  \renewcommand{\appendixpagename}%
    {Apêndices}%
}

\addto\captionsportuges{%
  \renewcommand{\appendixname}%
    {Apêndice}%
}

\addto\captionsportuges{%
  \renewcommand{\appendixtocname}%
    {Apêndices}%
}
} % para português
{} % nada a fazer para inglês


\DeclareRobustCommand{\apendices}{%
\appendixpage%
\appendix 
\renewcommand{\thechapter}{\Roman{chapter}}%
}

\DeclareRobustCommand{\anexos}{%
\pt-en{
\renewcommand{\appendixpagename}{Anexos}
\renewcommand{\appendixname}{Anexo}
\renewcommand{\appendixtocname}{Anexos}
}{
\renewcommand{\appendixpagename}{Annexes}
\renewcommand{\appendixname}{Annex}
\renewcommand{\appendixtocname}{Annexes}
}

\appendixpage
\appendix \renewcommand{\thechapter}{\Roman{chapter}}
}


\pt-en{
\DeclareRobustCommand{\agradecimentos}{%
\cleardoublepage
\vspace*{1cm}
\addcontentsline{toc}{chapter}{Agradecimentos}
\thispagestyle{plain}
{\LARGE \textit{Agradecimentos}}
}
}
{
\DeclareRobustCommand{\agradecimentos}{%
\cleardoublepage
\vspace*{1cm}
\addcontentsline{toc}{chapter}{Acknowledgements}
\thispagestyle{plain}
{\LARGE \textit{acknowledgements}}
}
}

%\addto\captionsportuges{%
  %\renewcommand{\bibname}%
 %   {Referências bibliográficas}%
%}

\maxtocdepth{subsection}
%http://tex.stackexchange.com/questions/3327/turn-on-subsection-numbering-in-memoir
\setsecnumdepth{subsection}
\newcommand{\rodape}[1]{\footnote{#1}}
% para palavras em inglês ou outras línguas diferentes do português
\newcommand{\ing}[1]{\textit{#1}}
\captionnamefont{\bfseries}


% configuracao da package listings para listagens de código
% http://www.ctan.org/pkg/listings
% http://tex.stackexchange.com/questions/24528/having-problems-with-listings-and-utf-8-can-it-be-fixed
% mais informação em https://en.wikibooks.org/wiki/LaTeX/Source_Code_Listings
\lstset{
frame=single,
basicstyle=\footnotesize,
breakatwhitespace=false,
breaklines=true,
xleftmargin=0.7cm,
xrightmargin=0.5cm,
numbers=left,
stepnumber=1,
numbersep=4pt,
numberstyle=\tiny,
keepspaces=true,
%backgroundcolor=\color{white},
showspaces=false,
showstringspaces=false,
showtabs=false,
tabsize=1,
captionpos=b,
breaklines=true,
breakatwhitespace=false,
escapeinside={\%*}{*)}, 
extendedchars=true,
inputencoding=utf8,
literate={á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ú}{{\'u}}1
  {Á}{{\'A}}1 {É}{{\'E}}1 {Í}{{\'I}}1 {Ó}{{\'O}}1 {Ú}{{\'U}}1
  {à}{{\`a}}1 {è}{{\`e}}1 {ì}{{\`i}}1 {ò}{{\`o}}1 {ù}{{\`u}}1
  {À}{{\`A}}1 {È}{{\'E}}1 {Ì}{{\`I}}1 {Ò}{{\`O}}1 {Ù}{{\`U}}1
  {ä}{{\"a}}1 {ë}{{\"e}}1 {ï}{{\"i}}1 {ö}{{\"o}}1 {ü}{{\"u}}1
  {Ä}{{\"A}}1 {Ë}{{\"E}}1 {Ï}{{\"I}}1 {Ö}{{\"O}}1 {Ü}{{\"U}}1
  {â}{{\^a}}1 {ê}{{\^e}}1 {î}{{\^i}}1 {ô}{{\^o}}1 {û}{{\^u}}1
  {Â}{{\^A}}1 {Ê}{{\^E}}1 {Î}{{\^I}}1 {Ô}{{\^O}}1 {Û}{{\^U}}1
  {Ã}{{\~A}}1 {ã}{{\~a}}1 {Õ}{{\~O}}1 {õ}{{\~o}}1
  {œ}{{\oe}}1 {Œ}{{\OE}}1 {æ}{{\ae}}1 {Æ}{{\AE}}1 {ß}{{\ss}}1
  {ű}{{\H{u}}}1 {Ű}{{\H{U}}}1 {ő}{{\H{o}}}1 {Ő}{{\H{O}}}1
  {ç}{{\c c}}1 {Ç}{{\c C}}1 {ø}{{\o}}1 {å}{{\r a}}1 {Å}{{\r A}}1
  {€}{{\euro}}1 {£}{{\pounds}}1 {«}{{\guillemotleft}}1
  {»}{{\guillemotright}}1 {ñ}{{\~n}}1 {Ñ}{{\~N}}1 {¿}{{?`}}1 
}

% directoria para as figuras
\graphicspath{{figuras/}}

\newcommand{\Java}{Java\textsuperscript{TM}}

\endinput
