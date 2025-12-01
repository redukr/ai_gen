a = Analysis(
    ['app.py'],
    pathex=['D:/PRJ/ai_generator'],
    binaries=[],
    datas=[
        # Лишаємо тільки код, без models
        ('tools/*.py', 'tools'),
    ],
    hiddenimports=[
        'tools.generator',
        'tools.image_tools',
        'tools.csv_loader',
        # Додай бібліотеки, які використовуєш
        'diffusers',
        'transformers',
        'torch',
        'torch._C',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)