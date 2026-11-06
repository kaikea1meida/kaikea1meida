import html
import os

largura = 820   # Largura levemente ajustada para dar espaço e respiro
altura = 460    # Altura compacta
fps = 0.1

inicio_frame = 13
fim_frame = 29
total_frames = (fim_frame - inicio_frame) + 1
duracao_total = total_frames * fps
porcentagem_visivel = 100 / total_frames

svg = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {largura} {altura}" width="100%" height="100%">',
    '<style>',
    '  .frame { font-family: monospace; font-size: 10px; fill: #e5e5e5; opacity: 0; }',
    '  .hud-title { font-family: monospace; font-size: 12px; fill: #e06c75; font-weight: bold; }',
    '  .hud-line  { font-family: monospace; font-size: 12px; fill: #5c6370; }',
    '  .hud-key   { font-family: monospace; font-size: 12px; fill: #98c379; font-weight: bold; }',
    '  .hud-val   { font-family: monospace; font-size: 12px; fill: #c9d1d9; }',
    '  .hud-cat   { font-family: monospace; font-size: 12px; fill: #e5c07b; font-weight: bold; }',
    '  @keyframes anim {',
    f'    0%, {porcentagem_visivel:.2f}% {{ opacity: 1; }}',
    f'    {porcentagem_visivel + 0.01:.2f}%, 100% {{ opacity: 0; }}',
    '  }',
]

for i in range(1, total_frames + 1):
    delay = (i - 1) * fps
    svg.append(f'  .f{i} {{ animation: anim {duracao_total:.1f}s infinite; animation-delay: {delay:.1f}s; }}')
svg.append('</style>')

# 1. Avatar animado bem à esquerda (encostado)
svg.append('<g transform="translate(-15, 0) scale(0.43)">')

caminho_pasta = 'image'
for i, num_arquivo in enumerate(range(inicio_frame, fim_frame + 1), 1):
    nome_arquivo = f'{caminho_pasta}/ascii-art({num_arquivo}).txt'
    svg.append(f'  <text class="frame f{i}" x="0" y="0">')
    
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                linha_limpa = html.escape(linha.rstrip('\n'))
                linha_limpa = linha_limpa.replace(' ', '&#160;')
                svg.append(f'    <tspan x="0" dy="11px">{linha_limpa}</tspan>')
    else:
        print(f"Aviso: {nome_arquivo} não encontrado.")
        
    svg.append('  </text>')

svg.append('</g>')

# 2. Bloco do HUD jogado para a direita com um espaço bacana em relação ao avatar
hud_elements = [
    '<g transform="translate(370, 18)">',
    '  <text class="hud-title" x="0" y="0">kaike@ufrrj-pc</text>',
    '  <text class="hud-line" x="0" y="20">---------------------------------------------------</text>',
    '  <text class="hud-key" x="0" y="42">OS:</text><text class="hud-val" x="85" y="42">Ubuntu Linux (x86_64)</text>',
    '  <text class="hud-key" x="0" y="62">Host:</text><text class="hud-val" x="85" y="62">Custom Desktop Rig</text>',
    '  <text class="hud-key" x="0" y="82">Kernel:</text><text class="hud-val" x="85" y="82">Linux (Custom)</text>',
    '  <text class="hud-key" x="0" y="102">Uptime:</text><text class="hud-val" x="85" y="102">2nd Semester (2026)</text>',
    '  <text class="hud-key" x="0" y="122">Theme:</text><text class="hud-val" x="85" y="122">Me</text>',
    '  <text class="hud-key" x="0" y="142">Memory:</text><text class="hud-val" x="85" y="142">0 / 0MiB</text>',
    '  <text class="hud-key" x="0" y="162">GPU:</text><text class="hud-val" x="85" y="162">AMD Radeon RX 580</text>',
    '  <text class="hud-key" x="0" y="182">Shell:</text><text class="hud-val" x="85" y="182">bash</text>',
    '  <text class="hud-key" x="0" y="202">Terminal:</text><text class="hud-val" x="85" y="202">VS Code Terminal</text>',
    '  <text class="hud-key" x="0" y="222">Institution:</text><text class="hud-val" x="110" y="222">UFRRJ (IM)</text>',
    '  <text class="hud-key" x="0" y="242">Degree:</text><text class="hud-val" x="85" y="242">Computer Science</text>',
    '  <text class="hud-key" x="0" y="262">Language:</text><text class="hud-val" x="90" y="262">C (Primary)</text>',
    '  <text class="hud-key" x="0" y="282">Interests:</text><text class="hud-val" x="90" y="282">Graphs &amp; Data Structs. &amp; Comp. Arch.</text>',
    '  <text class="hud-key" x="0" y="302">Editor:</text><text class="hud-val" x="85" y="302">VS Code / Terminal</text>',
    '  <text class="hud-key" x="0" y="322">Git:</text><text class="hud-val" x="50" y="322">Git &amp; GitHub</text>',
    '  <text class="hud-line" x="0" y="342">---------------------------------------------------</text>',
    '  <text class="hud-cat" x="0" y="366">Contact:</text>',
    '  <text class="hud-key" x="0" y="386">GitHub:</text><text class="hud-val" x="80" y="386">@kaikea1meida || kaikeaes@gmail.com</text>',
    '  <text class="hud-key" x="0" y="406">Status:</text><text class="hud-val" x="80" y="406">Building C Games and Chordal project</text>',
    '</g>'
]

svg.extend(hud_elements)
svg.append('</svg>')

with open('avatar-animado0.svg', 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg))

print("SVG gerado com o avatar na esquerda, HUD na direita e espaçamento ideal!")