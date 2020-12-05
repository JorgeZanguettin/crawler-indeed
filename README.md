# **Indeed**

## O que é Indeed?

O Indeed é o site de empregos com mais de 250 milhões de visitantes únicos por mês. O Indeed está presente em mais de 60 países e 28 idiomas, abrangendo 94% do PIB mundial.

## **Dados Coletados**

## Variaveis

```yaml
{
titulo_vaga : String,
nome_empresa : String,
resumo_vaga : String,
link_vaga : String,
vaga_postada_há : String,
data_coleta : Datetime
}
```

## Amostra

| TITULO_VAGA | NOME_EMPRESA | RESUMO_VAGA | LINK_VAGA | VAGA_POSTADA_HÁ | DATA_COLETA | 
| --- | --- | --- | --- | --- | --- |
| Desenvolvedor Mainframe | Indra |  | https://www.indeed.com.br/rc/clk?jk=59a198c0268ec286&fccid=7ebf81831a412784&vjs=3 |  | 2020-12-05 08:54:06.799823 |
| Desenvolvedor(a) HTML5/CSS | Storm X | Atribuições: Desenvolvimento de sites, portais e apps web, utilizando as melhores práticas e tecnologias.Criativo(a) na resolução de problemas. | https://www.indeed.com.br/rc/clk?jk=4b2fb1f3a1cb32d0&fccid=f2a0127ff0966d4e&vjs=3 | há 2 dias | 2020-12-05 08:54:06.803801 |
| Desenvolvedor Front-end PJ | Impacta Tecnologia | Irá desenvolver aplicações front-end, utilizando tecnologias como HTML, CSS, Javascript e Vue.js.Ter conhecimento básico de GIT e PHP. | https://www.indeed.com.br/company/Impacta-Tecnologia/jobs/Desenvolvedor-Front-End-Pj-7b1a616199a48fdb?fccid=f01ddb6f28b6b23d&vjs=3 | há 3 dias | 2020-12-05 08:54:06.807888 |
| Desenvolvedor Frontend (100% Remoto) | Villadal RH | Buscamos Desenvolvedores Perfis Pleno e/ou Sr para atuar em empresa de tecnologia.Experiência com Angular 2+ e TypeScript.Duração do contrato: 3000000 meses. | https://www.indeed.com.br/company/Villadal-RH/jobs/Desenvolvedor-Frontend-7e455727e146743a?fccid=8148da4728d3df93&vjs=3 | há 4 dias | 2020-12-05 08:54:06.812954 |
| Desenvolvedor Junior | YKP |  | https://www.indeed.com.br/company/YKP/jobs/Desenvolvedor-Junior-3de364af1b86ed48?fccid=d6b5c840e12c3f9f&vjs=3 |  | 2020-12-05 08:54:06.814957 |

## Como executar?

1. Faça o download e instalação do Python 3 [Aqui](https://www.python.org/).
2. Direcione o seu bash de preferencia a pasta raiz do repositorio e instale as dependencias utilizando o comando ```pip install -r requirements.txt``` ou ```pip3 install -r requirements.txt``` .
3. Execute o Crawler com o comando ```python indeed.py Cargo Cidade``` ou ```python3 indeed.py Cargo Cidade``` .
4. Pronto! Os dados coletados serão armazenados em um arquivo CSV na raiz do projeto com o nome **vagas.csv**.
