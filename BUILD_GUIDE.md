# Guía de Compilación - Isekai MMORPG V0.1

## Opción 1: Compilar localmente (Recomendado para desarrollo)

### Requisitos
- Python 3.7+
- Git
- Zip (instalado por defecto en Linux/macOS, incluido en Windows 10+)

### Pasos

1. **Clonar el repositorio**
```bash
git clone https://github.com/robletodariel-create/isekai-mmorpg.git
cd isekai-mmorpg
```

2. **Ejecutar el script de compilación**
```bash
python3 build_modpack.py
```

3. **Verificar que el ZIP se creó**
```bash
ls -lh isekai_races_v0.1_curseforge.zip
```

El archivo `isekai_races_v0.1_curseforge.zip` estará en la raíz del repositorio.

---

## Opción 2: Compilar manualmente en Windows

Si prefieres compilar sin usar Python:

1. Abre el Explorador de Archivos
2. Ve a la carpeta `curseforge/`
3. Selecciona:
   - `manifest.json`
   - `overrides/` (carpeta completa)
4. Haz clic derecho → "Enviar a" → "Carpeta comprimida (ZIP)"
5. Renombra el ZIP a `isekai_races_v0.1_curseforge.zip`

**Importante:** El ZIP debe contener `manifest.json` en la raíz, no en una carpeta adicional.

---

## Opción 3: Compilar manualmente en Linux/macOS

```bash
cd curseforge
zip -r ../isekai_races_v0.1_curseforge.zip manifest.json overrides/
cd ..
```

---

## Instalación en CurseForge

1. **Abre CurseForge Launcher**
2. **Clic en "Create Custom Profile"**
3. **Selecciona "Import"**
4. **Busca el archivo `isekai_races_v0.1_curseforge.zip`**
5. **Haz clic en "Create Instance"**
6. **Selecciona Minecraft 1.21.1 + Fabric**
7. **Haz clic en "Create"**

---

## Instalación manual (sin CurseForge)

Si prefieres instalar directamente:

1. Descarga y extrae `isekai_races_v0.1_curseforge.zip`
2. Copia la carpeta `overrides/datapacks/isekai/` a:
   ```
   .minecraft/datapacks/
   ```
3. Inicia Minecraft
4. Crea un mundo nuevo
5. Ve a Configuración → Mod Menu (si está instalado) → Origins
6. Selecciona tu raza

---

## Estructura del ZIP (Verificación)

El ZIP debe contener exactamente esto en la raíz:

```
isekai_races_v0.1_curseforge.zip
├── manifest.json
└── overrides/
    └── datapacks/
        └── isekai/
            ├── pack.mcmeta
            └── data/
                ├── minecraft/
                │   └── tags/
                │       └── function/
                │           ├── load.json
                │           └── tick.json
                └── isekai/
                    ├── origins/
                    │   ├── humano.json
                    │   ├── goblin.json
                    │   ├── beastkin.json
                    │   ├── orco.json
                    │   └── slime.json
                    └── functions/
                        ├── load.mcfunction
                        └── tick.mcfunction
```

Para verificar el contenido del ZIP:

**Linux/macOS:**
```bash
unzip -l isekai_races_v0.1_curseforge.zip
```

**Windows (PowerShell):**
```powershell
Expand-Archive -Path isekai_races_v0.1_curseforge.zip -DestinationPath temp
ls temp -Recurse
Remove-Item temp -Recurse
```

---

## Solución de Problemas

### El ZIP no se crea
- Verifica que todos los archivos en `curseforge/` existan
- Asegúrate de tener permisos de escritura en el directorio
- Intenta ejecutar el script con permisos elevados (sudo/Admin)

### CurseForge no reconoce el ZIP
- Verifica que `manifest.json` esté en la raíz del ZIP
- No debe haber una carpeta adicional envolviendo los archivos
- El ZIP debe ser válido (no corrupto)

### Las razas no aparecen en el juego
- Asegúrate de tener Origins instalado
- Recarga el datapack: `/reload`
- Crea un mundo nuevo
- Comprueba que Origins esté activo en Mod Menu

---

## Actualizaciones Futuras

Para modificar las razas o agregar nuevas:

1. Edita los archivos JSON en `curseforge/overrides/datapacks/isekai/data/isekai/origins/`
2. Ejecuta: `python3 build_modpack.py`
3. El nuevo ZIP estará listo para importar

---

**Versión:** V0.1  
**Minecraft:** 1.21.1 Fabric  
**Última actualización:** 2026-09-10
