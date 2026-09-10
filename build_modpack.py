#!/usr/bin/env python3
"""
Script para compilar el modpack CurseForge de Isekai MMORPG
Genera: isekai_races_v0.1_curseforge.zip
"""

import os
import shutil
import json
from pathlib import Path

def validate_files():
    """Valida que existan todos los archivos necesarios"""
    required_files = [
        'curseforge/manifest.json',
        'curseforge/overrides/datapacks/isekai/pack.mcmeta',
        'curseforge/overrides/datapacks/isekai/data/isekai/origins/humano.json',
        'curseforge/overrides/datapacks/isekai/data/isekai/origins/goblin.json',
        'curseforge/overrides/datapacks/isekai/data/isekai/origins/beastkin.json',
        'curseforge/overrides/datapacks/isekai/data/isekai/origins/orco.json',
        'curseforge/overrides/datapacks/isekai/data/isekai/origins/slime.json',
        'curseforge/overrides/datapacks/isekai/data/minecraft/tags/function/load.json',
        'curseforge/overrides/datapacks/isekai/data/minecraft/tags/function/tick.json',
        'curseforge/overrides/datapacks/isekai/data/isekai/functions/load.mcfunction',
        'curseforge/overrides/datapacks/isekai/data/isekai/functions/tick.mcfunction',
    ]
    
    print("✓ Validando archivos necesarios...")
    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"❌ Error: Archivo no encontrado: {file_path}")
            return False
        print(f"  ✓ {file_path}")
    
    return True

def validate_json(file_path):
    """Valida que un archivo JSON sea válido"""
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError as e:
        print(f"❌ JSON inválido en {file_path}: {e}")
        return False

def validate_manifest():
    """Valida que manifest.json sea correcto"""
    print("\n✓ Validando manifest.json...")
    if not validate_json('curseforge/manifest.json'):
        return False
    
    with open('curseforge/manifest.json', 'r') as f:
        manifest = json.load(f)
    
    required_keys = ['minecraft', 'manifestType', 'manifestVersion', 'name', 'version', 'overrides']
    for key in required_keys:
        if key not in manifest:
            print(f"❌ Falta la clave '{key}' en manifest.json")
            return False
        print(f"  ✓ {key}: {manifest[key]}")
    
    return True

def create_zip():
    """Crea el archivo ZIP del modpack"""
    print("\n✓ Creando ZIP...")
    
    # Limpiar ZIP anterior si existe
    zip_path = 'isekai_races_v0.1_curseforge.zip'
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"  ✓ ZIP anterior eliminado")
    
    # Crear ZIP desde la carpeta curseforge
    # Asegurarse de que la raíz del ZIP contiene manifest.json y overrides/
    try:
        shutil.make_archive(
            'isekai_races_v0.1_curseforge',  # nombre base (sin .zip)
            'zip',  # formato
            'curseforge'  # carpeta base (se incluye todo dentro sin la carpeta padre)
        )
        print(f"  ✓ ZIP creado: {zip_path}")
        return True
    except Exception as e:
        print(f"❌ Error al crear ZIP: {e}")
        return False

def verify_zip():
    """Verifica el contenido del ZIP"""
    print("\n✓ Verificando contenido del ZIP...")
    import zipfile
    
    zip_path = 'isekai_races_v0.1_curseforge.zip'
    if not os.path.exists(zip_path):
        print(f"❌ Error: {zip_path} no existe")
        return False
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            
            # Verificar estructura raíz
            print(f"  ✓ Total de archivos: {len(file_list)}")
            
            # Archivos críticos que deben estar en la raíz
            critical_files = [
                'manifest.json',
                'overrides/',
                'overrides/datapacks/isekai/pack.mcmeta',
                'overrides/datapacks/isekai/data/isekai/origins/humano.json',
                'overrides/datapacks/isekai/data/isekai/origins/goblin.json',
                'overrides/datapacks/isekai/data/isekai/origins/beastkin.json',
                'overrides/datapacks/isekai/data/isekai/origins/orco.json',
                'overrides/datapacks/isekai/data/isekai/origins/slime.json',
            ]
            
            for critical in critical_files:
                found = False
                for f in file_list:
                    if f == critical or f.startswith(critical):
                        found = True
                        break
                
                if found:
                    print(f"  ✓ {critical}")
                else:
                    print(f"  ⚠ {critical} - NO ENCONTRADO")
            
            # Mostrar primeros 10 archivos
            print(f"\n  Primeros 10 archivos del ZIP:")
            for f in sorted(file_list)[:10]:
                print(f"    {f}")
            
            if 'manifest.json' not in file_list:
                print("❌ Error: manifest.json no está en la raíz del ZIP")
                return False
            
            return True
    except Exception as e:
        print(f"❌ Error al verificar ZIP: {e}")
        return False

def main():
    print("=" * 60)
    print("🔨 Compilador de Modpack CurseForge - Isekai MMORPG V0.1")
    print("=" * 60)
    
    # Cambiar al directorio del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print(f"\n📍 Directorio de trabajo: {os.getcwd()}")
    
    # Validar archivos
    if not validate_files():
        print("\n❌ Validación de archivos fallida")
        return False
    
    # Validar manifest.json
    if not validate_manifest():
        print("\n❌ Validación de manifest.json fallida")
        return False
    
    # Crear ZIP
    if not create_zip():
        print("\n❌ Creación de ZIP fallida")
        return False
    
    # Verificar ZIP
    if not verify_zip():
        print("\n❌ Verificación de ZIP fallida")
        return False
    
    print("\n" + "=" * 60)
    print("✅ ¡Compilación completada exitosamente!")
    print("=" * 60)
    print(f"\n📦 Archivo generado: isekai_races_v0.1_curseforge.zip")
    print(f"📊 Tamaño: {os.path.getsize('isekai_races_v0.1_curseforge.zip') / 1024:.2f} KB")
    print(f"\n✓ Listo para importar en CurseForge")
    print(f"✓ Descárgalo desde: https://github.com/robletodariel-create/isekai-mmorpg/releases")
    
    return True

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
