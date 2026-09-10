#!/bin/bash

# Script para generar isekai_races_v0.1.zip
# Uso: bash build_zip.sh

set -e

echo "📦 Compilando Isekai MMORPG - Sistema de Razas V0.1..."

# Navegar al directorio del datapack
cd datapack/isekai

# Verificar que existan los archivos necesarios
echo "✓ Verificando archivos..."
if [ ! -f "pack.mcmeta" ]; then
    echo "❌ Error: pack.mcmeta no encontrado"
    exit 1
fi

if [ ! -d "data" ]; then
    echo "❌ Error: carpeta data/ no encontrada"
    exit 1
fi

# Verificar que existan todos los origins
origins=(
    "data/isekai/origins/humano.json"
    "data/isekai/origins/goblin.json"
    "data/isekai/origins/beastkin.json"
    "data/isekai/origins/orco.json"
    "data/isekai/origins/slime.json"
)

for origin in "${origins[@]}"; do
    if [ ! -f "$origin" ]; then
        echo "❌ Error: $origin no encontrado"
        exit 1
    fi
done

echo "✓ Todos los archivos verificados"

# Crear el ZIP
echo "📝 Creando ZIP..."
rm -f "../../isekai_races_v0.1.zip" 2>/dev/null || true
zip -r "../../isekai_races_v0.1.zip" pack.mcmeta data/

echo "✓ ZIP creado: isekai_races_v0.1.zip"
echo ""
echo "📊 Contenido del ZIP:"
unzip -l "../../isekai_races_v0.1.zip"

echo ""
echo "✅ ¡ZIP compilado exitosamente!"
echo "📍 Ubicación: isekai_races_v0.1.zip"
echo ""
echo "Para instalar:"
echo "1. Descarga isekai_races_v0.1.zip"
echo "2. Extrae la carpeta en: .minecraft/saves/<MUNDO>/datapacks/"
echo "3. Ejecuta: /reload"
echo "4. ¡Disfruta de las razas!"
