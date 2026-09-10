# Isekai MMORPG - Load Function
# Ejecutado una sola vez cuando se carga el datapack

# Inicializar scoreboards
scoreboard objectives add isekai_level dummy "Nivel Isekai"
scoreboard objectives add isekai_exp dummy "Experiencia Isekai"
scoreboard objectives add isekai_strength dummy "Fuerza"
scoreboard objectives add isekai_defense dummy "Defensa"
scoreboard objectives add isekai_intelligence dummy "Inteligencia"
scoreboard objectives add isekai_dexterity dummy "Destreza"
scoreboard objectives add isekai_vitality dummy "Vitalidad"

# Mensaje de confirmación
tellraw @a [{"text": "","color": "green"},{"text": "[Isekai MMORPG V0.1]","color": "gold"},{"text": " Datapack cargado correctamente","color": "green"}]

# Log en la consola
say Isekai MMORPG V0.1 - Sistema de Razas cargado
