from collections import namedtuple



Class = namedtuple('Class', 'subject teacher room')



SCHEDULE = [

    # Monday is the 0 index

    [ Class('Gestão Ambiental', 'Eliane Melo', 'Sala 18'),

      Class('Gestão de Pessoas', 'Sandra Aparecida', 'lab 3') ],

    # Tuesday

    [ Class('Inglês III', 'Thiago Rebeca', 'Sala 19'),

      Class('Contabilidade', 'Tessa Coltro', 'Sala 18') ],

    # Wednesday

    [ Class('Gestão de Pessoas', 'Sandra Aparecida', 'Lab 3'),

      Class('Estatística', 'Diogo Robies', 'Sala 18') ],

    # Thursday

    [ Class('Banco de Dados', 'Maria Janaina', 'Lab 1'),

      Class('Banco de Dados', 'Maria Janaina', 'Lab 1') ],

    # Friday

    [ Class('Engenharia de Software', 'Aanderson Barbosa', 'Sala 2'),

      Class('Engenharia de Software', 'Anderson Barbosa', 'Sala 2') ],

    # Saturday

    [ Class('Atividades de Projetos II/III', 'Anderson Barbosa', 'Lab 3') ]

]
