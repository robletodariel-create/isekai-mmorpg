#!/usr/bin/env python3
"""
Script para compilar el modpack CurseForge de Isekai MMORPG
Genera: isekai_races_v0.1_curseforge.zip
"""
import os
import shutil
import json
import sys

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
    missing = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing.append(file_path)
        else:
            print(f"  ✓ {file_path}")
    if missing:
        print("\n❌ Archivos faltantes:")
        for m in missing:
            print(f"  - {m}")
        return False
    return True

def validate_json(file_path):
    """Valida que un archivo JSON sea válido"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True
    except json.JSONDecodeError as e:
        print(f"❌ JSON inválido en {file_path}: {e}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                snippet = f.read(500)
                print("Contenido (primeros 500 caracteres):")
                print(snippet)
        except Exception:
            pass
        return False
    except Exception as e:
        print(f"❌ Error leyendo {file_path}: {e}")
        return False

def validate_manifest():
    """Valida que manifest.json sea correcto"""
    print("\n✓ Validando manifest.json...")
    if not validate_json('curseforge/manifest.json'):
        return False

    try:
        with open('curseforge/manifest.json', 'r', encoding='utf-8') as f:
            manifest = json.load(f)
    except Exception as e:
        print(f"❌ Error al cargar manifest.json: {e}")
        return False

    required_keys = ['minecraft', 'manifestType', 'manifestVersion', 'name', 'version', 'overrides']
    for key in required_keys:
        if key not in manifest:
            print(f"❌ Falta la clave '{key}' en manifest.json")
            return False
        print(f"  ✓ {key}: {manifest[key]}")
    return True

def create_zip():
    """Crea el archivo ZIP del modpack (CurseForge)"""
    print("\n✓ Creando ZIP CurseForge...")
    zip_path = 'isekai_races_v0.1_curseforge.zip'
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"  ✓ ZIP anterior eliminado")

    try:
        shutil.make_archive('isekai_races_v0.1_curseforge', 'zip', 'curseforge')
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
            print(f"  ✓ Total de archivos: {len(file_list)}")
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
                found = any(f == critical or f.startswith(critical) for f in file_list)
                if found:
                    print(f"  ✓ {critical}")
                else:
                    print(f"  ⚠ {critical} - NO ENCONTRADO")
            print("\n  Primeros 10 archivos del ZIP:")
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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"\n📍 Directorio de trabajo: {os.getcwd()}")

    if not validate_files():
        print("\n❌ Validación de archivos fallida")
        return False

    if not validate_manifest():
        print("\n❌ Validación de manifest.json fallida")
        return False

    if not create_zip():
        print("\n❌ Creación de ZIP fallida")
        return False

    if not verify_zip():
        print("\n❌ Verificación de ZIP fallida")
        return False

    print("\n" + "=" * 60)
    print("✅ ¡Compilación completada exitosamente!")
    print("=" * 60)
    print(f"\n📦 Archivo generado: isekai_races_v0.1_curseforge.zip")
    try:
        print(f"📊 Tamaño: {os.path.getsize('isekai_races_v0.1_curseforge.zip') / 1024:.2f} KB")
    except Exception:
        pass
    print(f"\n✓ Listo para importar en CurseForge")
    return True

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception:
        import traceback
        print("❌ Excepción no controlada durante la ejecución:")
        traceback.print_exc()
        sys.exit(1)
