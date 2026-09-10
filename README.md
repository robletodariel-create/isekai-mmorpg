# Isekai MMORPG - Modpack para Minecraft 1.21.1

Sistema de razas MMORPG/Isekai para Minecraft Java 1.21.1 usando **Fabric** y el mod **Origins**.

## V0.1 - Sistema de Razas

Esta es la primera versión del modpack que incluye 5 razas seleccionables mediante Origins.

### Razas Disponibles

1. **Humano** (`isekai:humano`) - Raza equilibrada
2. **Goblin** (`isekai:goblin`) - Raza pequeña y rápida
3. **Beastkin** (`isekai:beastkin`) - Raza animal humanoide
4. **Orco** (`isekai:orco`) - Raza fuerte y resistente
5. **Slime** (`isekai:slime`) - Raza especial gelatinosa

## Requisitos

- **Minecraft Java Edition 1.21.1**
- **Fabric Loader** (última versión)
- **Fabric API** (compatible con 1.21.1)
- **Origins** (mod de Fabric para 1.21.1)

### Versión recomendada de Origins

- **Origins 1.13.0+** (official) o **Origins: Legacy** (para máxima compatibilidad)

## Instalación

### 1. Descargar el datapack

Descarga `isekai_races_v0.1.zip` desde este repositorio.

### 2. Extraer en la carpeta correcta

**Ruta en Windows:**
```
%APPDATA%\.minecraft\saves\<nombre_del_mundo>\datapacks\
```

**Ruta en macOS:**
```
~/Library/Application Support/minecraft/saves/<nombre_del_mundo>/datapacks/
```

**Ruta en Linux:**
```
~/.minecraft/saves/<nombre_del_mundo>/datapacks/
```

### 3. Crear un nuevo mundo

1. Abre Minecraft con Fabric
2. Crea un mundo **nuevo**
3. En la pantalla de creación de mundo, asegúrate de que los datapacks están **habilitados**
4. Inicia el mundo

### 4. Seleccionar tu raza

1. Una vez dentro del mundo, presiona **ESC**
2. Ve a **Configuración** → **Mod Menu** (si está instalado) → **Origins**
3. O presiona **O** en el teclado (atajo por defecto de Origins)
4. Selecciona una de las 5 razas disponibles
5. Tu selección se aplicará inmediatamente

## Estructura del Proyecto

```
isekai-mmorpg/
├── README.md                          # Este archivo
├── datapack/
│   └── isekai/                        # Datapack principal
│       ├── pack.mcmeta                # Metadatos del datapack
│       └── data/
│           ├── minecraft/             # Funciones del sistema Minecraft
│           │   └── tags/
│           │       └── function/
│           │           ├── load.json
│           │           └── tick.json
│           └── isekai/                # Namespace personalizado
│               ├── origins/           # Definiciones de Origins
│               │   ├── humano.json
│               │   ├── goblin.json
│               │   ├── beastkin.json
│               │   ├── orco.json
│               │   └── slime.json
│               └── functions/         # Funciones personalizadas
│                   ├── load.mcfunction
│                   └── tick.mcfunction
```

## ¿Dónde está el ZIP?

El archivo `isekai_races_v0.1.zip` se encuentra en la raíz del repositorio.

**Contiene exactamente:**
```
pack.mcmeta
data/
  minecraft/
    tags/
      function/
        load.json
        tick.json
  isekai/
    origins/
      humano.json
      goblin.json
      beastkin.json
      orco.json
      slime.json
    functions/
      load.mcfunction
      tick.mcfunction
```

## Solución de Problemas

### Las razas no aparecen

1. **Verifica que Origins esté instalado**
   - Abre el juego y busca Origins en Mod Menu o presiona O

2. **Recarga el datapack**
   - Escribe: `/reload`
   - Cierra y abre el mundo nuevamente

3. **Comprueba que el datapack esté habilitado**
   - Escribe: `/datapack list`
   - Deberías ver `isekai` en la lista

4. **Verifica los logs**
   - Busca errores en `%APPDATA%\.minecraft\logs\latest.log`
   - Los errores de Origins aparecerán en los logs

### El datapack carga pero no funciona

1. Asegúrate de tener **Fabric API** instalado
2. Verifica la versión de **Minecraft 1.21.1**
3. Borra la carpeta `world` y crea un mundo nuevo
4. Comprueba que el ZIP contenga `pack.mcmeta` y `data/` en la raíz

## Características de V0.1

**Estado:** Versión de prueba
- ✅ 5 razas disponibles y seleccionables
- ✅ Sistema de carga de datapack
- ✅ Estructura base para futuros sistemas
- ⏳ Habilidades especiales (próximas versiones)
- ⏳ Sistema de experiencia y niveles (próximas versiones)
- ⏳ Clases y especializaciones (próximas versiones)

## Desarrollo Futuro

Próximas características planificadas:
- V0.2: Habilidades especiales por raza
- V0.3: Sistema de experiencia y niveles
- V0.4: Clases y especializaciones
- V0.5: Sistema de inventario expandido
- V1.0: Sistema completo de dungeons y bosses

## Licencia

Este proyecto es de código abierto. Siéntete libre de modificarlo y mejorarlo.

## Contacto

Para reportar problemas o sugerencias, abre un issue en el repositorio.

---

**Versión:** V0.1  
**Última actualización:** 2026-09-10  
**Compatibilidad:** Minecraft 1.21.1 Fabric + Origins
