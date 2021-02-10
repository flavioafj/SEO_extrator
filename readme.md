Cole em três células vizinhas
=PROCURAR("?q=";Tabela1[@link])
=PROCURAR("&sa=";Tabela1[@link])
=EXT.TEXTO(Tabela1[@link];LC[-2]+3;LC[-1]-LC[-2]-3)
