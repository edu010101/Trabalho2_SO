# Simulador de Algoritmos de Escalonamento

Este projeto visa simular os seguintes algoritmos de escalonamento:

- FCFS - First-come,First-served
- SJF - Shortest Job First (preemptivo e não preemptivo)
- Prioridade
- Round Robin

A simulação será feita utilizando uma interface gráfica, em que também será possível comparar o tempo de cada algoritmo de escalonamento 

Esse projeto pode ser acessado também no [GitHub](https://github.com/edu010101/Trabalho2_SO.git).

## Visão Geral

<!--TODO-->

## Setup

### Anaconda

o projeto possui dependências de bibliotecas externas. É recomendado que seja utilizado um ambiente virtual para não causar riscos a seu ambiente atual. Para criar um ambiente virtual usando Anaconda, execute os comandos:

```bash
conda create --name trab_SO python=3.10
conda activate trab_SO
```

Para construir o projeto, abra o terminal na mesma pasta em que esse README se encontra, e execute os seguintes comandos:
```bash
pip install -r requirements.txt
```

## Execução

Para executar o programa, execute o seguinte comando no terminal:

```bash
python main.py
```

## Uso

A interface oferece a possibilidade de escolher o scheduler de interesse e observar os resultados do processamento no lado direito.
Para testar um scheduler basta selecionar sua aba no menu superior e clicar no botão "Run".

### Alterando os processos

Para mudar os processos que estão sendo processados, basta alterar o arquivo "processes_definition.json". Fique a vontade para adicionar, remover ou alterar quantos processos quiser, todavia, lembre-se que um processo sempre deve ser composto de 4 atributos:

- name (Nome do processo)
- duration (Tempo de burst do processo)
- arrival_time (Tempo em que o processo chega para ser executado)
- priority (Prioridade do processo, apenas será considerado caso esteja usando o scheduler "priority")


## Authors

|  [<img src="https://github.com/edu010101.png?size=460&u=071f7791bb03f8e102d835bdb9c2f0d3d24e8a34&v=4" width=115><br><sub>Eduardo Lopes</sub>](https://github.com/edu010101) |  [<img src="https://github.com/albertohiguti.png?size=460&u=071f7791bb03f8e102d835bdb9c2f0d3d24e8a34&v=4" width=115><br><sub>Alberto Higuti</sub>](https://github.com/albertohiguti) 
| :---: | :---: |

