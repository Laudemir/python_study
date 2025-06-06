#!/usr/bin/env python3
#
# @Autor....: Laudemir Oliveira
# @E-mail...: laudemir.oliveira@gmail.com
# @Date.....: 21-03-2024 - qui - 19:55
# @Version..: 2024-81
#
#
from datetime import datetime
from zoneinfo import ZoneInfo

data_hora_atual = datetime.now()

fuso_horario_sao_paulo = ZoneInfo('America/Sao_Paulo')
data_hora_sao_paulo = data_hora_atual.astimezone(fuso_horario_sao_paulo)

fuso_horario_ny = ZoneInfo('America/New_York')
data_hora_ny = data_hora_atual.astimezone(fuso_horario_ny)

print(f'Data/hora atual (fuso horario local): {data_hora_atual}')
print(f'Data/hora atual em São Paulo: {data_hora_sao_paulo}')
print(f'Data/hora atiaç em Nova York: {data_hora_ny}')
