#!/bin/bash
set -e
echo "📦 Generando isekai_races_v0.1.zip desde curseforge/overrides/datapacks/isekai..."
cd curseforge/overrides/datapacks/isekai
if [ ! -f "pack.mcmeta" ] || [ ! -d "data" ]; then
  echo "❌ pack.mcmeta o data/ no encontrado en curseforge/overrides/datapacks/isekai"
  exit 1
fi
zip -r ../../../../isekai_races_v0.1.zip pack.mcmeta data
echo "✓ isekai_races_v0.1.zip creado en la raíz del repo"
echo "3. Ejecuta: /reload"
echo "4. ¡Disfruta de las razas!"
