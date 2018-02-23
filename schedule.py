from collections import namedtuple

Class = namedtuple('Class', 'subject teacher room')

SCHEDULE = [
    # Monday is the 0 index
    [ Class('Processos Gerenciais', 'Sandra Ossada', 'Lab 3'),
      Class('Matemática Discreta', 'Aurimar Reis', 'Sala 17') ],
    # Tuesday
    [ Class('Inglês I', 'Marlucy Ribeiro', 'Sala 8'),
      Class('Fundamentos de TI', 'Anderson Coan', 'Lab 3') ],
    # Wednesday
    [ Class('Algoritmos', 'Maria Janaína Ferreira', 'Lab 3'),
      Class('Algoritmos', 'Maria Janaína Ferreira', 'Lab 3') ],
    # Thursday
    [ Class('Processos Gerenciais', 'Sandra Ossada', 'Lab 3'),
      Class('Matemática Discreta', 'Aurimar Reis', 'Sala 17') ],
    # Friday
    [ Class('Comunicação e Expressão', 'Flávio Pereira', 'Sala 17'),
      Class('Comunicação e Expressão', 'Flávio Pereira', 'Sala 17') ],
    # Saturday
    [ Class('Atividades ACC', 'Diogo Robles', 'Sala 18'),
      Class('Atividades ACC', 'Diogo Robles', 'Sala 18') ]
]
