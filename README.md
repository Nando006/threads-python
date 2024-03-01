# threads-python

Threads, também conhecidas como linhas de execução. Cada programa ou processo é organizado em threads, que formam tarefas independentes, mas relacionadas entre si.

Em termos simples, as threads permitem que um programa execute várias tarefas simultaneamente, o que é conhecido como paralelismo. Isso significa que seu programa pode agir como se tivesse vários aplicativos com partes de seu código atuando em paralelo no sistema.

As threads são escalonadas para executar na CPU, concorrendo pelo processador com outras threads que possam existir no programa. Elas compartilham o mesmo espaço de endereçamento do aplicativo em execução, o que torna a criação de uma thread mais eficiente em termos de processamento e memória do que a criação de um novo aplicativo.

A principal razão para a existência das threads é permitir que muitas atividades ocorram ao mesmo tempo em nossa aplicação. Além disso, o uso de threads pode tornar o modelo de programação mais simples, à medida que decompomos a aplicação em múltiplos threads que executam quase em paralelo.

