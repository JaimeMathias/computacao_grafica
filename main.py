import bpy

# Modela objeto a partir dos vertices, faces e edges
def mesh_build(verts, faces, edges):
    mymesh = bpy.data.meshes.new("Cube")
    myobject = bpy.data.objects.new("Cube", mymesh)

    bpy.context.collection.objects.link(myobject)

    mymesh.from_pydata(verts, [], faces)
    mymesh.update(calc_edges=True)
    
    return myobject


# Adiciona textura de uma imagem ao objeto passado
def draw_texture(obj, image):
    mat = bpy.data.materials.new(name = "New_Mat")
    mat.use_nodes = True
    
    principled_node = mat.node_tree.nodes["Principled BSDF"]
    
    texImage = mat.node_tree.nodes.new('ShaderNodeTexImage')
    texImage.image = bpy.data.images.load(image)
    mat.node_tree.links.new(principled_node.inputs['Base Color'], texImage.outputs['Color'])
        
    obj.data.materials.append(mat)


# Modela um "cubo" a partir de um ponto y e outros parametros passados
def draw_cube_y(altura, tamanho, comprimento, largura, ponto_central, y, image, offset = 0.01):
    comprimento = comprimento / 2.0
    ponto_1 = ponto_central - comprimento
    ponto_2 = ponto_central + comprimento
    
    if (largura > 0):
        verts = [
            (ponto_1, y + offset, altura),
            (ponto_1, y + offset, altura + tamanho),
            (ponto_2, y + offset, altura),
            (ponto_2, y + offset, altura + tamanho),
            
            (ponto_1, y + offset + largura, altura),
            (ponto_1, y + offset + largura, altura + tamanho),
            (ponto_2, y + offset + largura, altura),
            (ponto_2, y + offset + largura, altura + tamanho),
        ]
        faces = [
            (0,1,3,2),
            (4,5,7,6),
            
            (0,1,5,4),
            (2,3,7,6),
            (1,3,7,5),
            (0,2,6,4),
        ]
        
    else:
        verts = [
            (ponto_1, y + offset, altura),
            (ponto_1, y + offset, altura + tamanho),
            (ponto_2, y + offset, altura),
            (ponto_2, y + offset, altura + tamanho),
        ]
        faces = [
            (0,1,3,2),
        ]
    
    
    object = mesh_build(verts, faces, [])
    image_path = assets_folder + image
    draw_texture(object, image_path)


# Modela um "cubo" a partir de um ponto x e outros parametros passados
def draw_cube_x(altura, comprimento, tamanho, largura, ponto_central, x, image, offset = 0.001):
    tamanho = tamanho / 2.0
    ponto_1 = ponto_central - tamanho
    ponto_2 = ponto_central + tamanho

    if (largura > 0):
        verts = [
            (x + offset, ponto_1, altura),
            (x + offset, ponto_1, altura + comprimento),
            (x + offset, ponto_2, altura),
            (x + offset, ponto_2, altura + comprimento),
            
            (x + offset + largura, ponto_1, altura),
            (x + offset + largura, ponto_1, altura + comprimento),
            (x + offset + largura, ponto_2, altura),
            (x + offset + largura, ponto_2, altura + comprimento),
        ]
        faces = [
            (0,1,3,2),
            (4,5,7,6),
            
            (0,1,5,4),
            (2,3,7,6),
            (1,3,7,5),
            (0,2,6,4),
        ]
    else:
        verts = [
            (x + offset, ponto_1, altura),
            (x + offset, ponto_1, altura + comprimento),
            (x + offset, ponto_2, altura),
            (x + offset, ponto_2, altura + comprimento),
        ]
        faces = [
            (0,1,3,2),
        ]

    object = mesh_build(verts, faces, [])
    image_path = assets_folder + image
    draw_texture(object, image_path)


# Modela a casa
def draw_casa():
    verts = [
        (0, 0, 0), #0
        (0, 0, altura_casa), #1
        (0, largura_y, 0), #2
        (0, largura_y, altura_casa), #3
        (largura_x - jardim_x, largura_y, 0), #4
        (largura_x - jardim_x, largura_y, altura_casa), #5
        (largura_x - jardim_x, largura_y - jardim_y, 0), #6
        (largura_x - jardim_x, largura_y - jardim_y, altura_casa), #7
        (largura_x, largura_y - jardim_y, 0), #8
        (largura_x, largura_y - jardim_y, altura_casa), #9
        (largura_x, 0, 0), #10
        (largura_x, 0, altura_casa), #11
    ]

    faces = [
        (1,3,5,7,9,11), # Teto
        (0,2,4,6,8,10), # Chao
        (0,1,3,2),
        (2,3,5,4),
        (4,5,7,6),
        (6,7,9,8),
        (8,9,11,10),
        (10,11,1,0),
    ]

    object = mesh_build(verts, faces, [])
    image = assets_folder + "casa_pintura.jpg"
    draw_texture(object, image)


# Modela o telhado da casa
def draw_telhado():
    # Dimensões do telhado
    altura_telhado = 1
    telhado_x = (largura_x - jardim_x) / 2
    telhado_y = (largura_y - jardim_y) / 2
    telhado_offset = 0.2
    
    verts = [
        (0 - telhado_offset, 0 - telhado_offset, altura_casa), #0
        (0 - telhado_offset, largura_y, altura_casa), #1
        (largura_x - jardim_x + telhado_offset, largura_y, altura_casa), #2
        (largura_x - jardim_x + telhado_offset, largura_y - jardim_y + telhado_offset, altura_casa), #3
        (largura_x, largura_y - jardim_y + telhado_offset, altura_casa), #4
        (largura_x, 0 - telhado_offset, altura_casa), #5
        
        (telhado_x, largura_y, altura_casa + altura_telhado), #6
        (largura_x, telhado_y, altura_casa + altura_telhado), #7
        (telhado_y, telhado_x, altura_casa + altura_telhado),  #8
    ]

    faces = [
        (1, 6, 2),
        (1, 0, 8, 6),
        (2, 6, 8, 3),
        (3, 8, 7, 4),
        (4, 7, 5),
        (5, 7, 8, 0),
        
        (0, 1, 2, 3, 4, 5), # "Chao do telhado"
    ]

    object = mesh_build(verts, faces, [])
    image = assets_folder + "marrom.jpg"
    draw_texture(object, image)



assets_folder = "C:\\Users\\jaime\\Desktop\\4 Ano - 1° Semestre\\COMPUTAÇÃO GRÁFICA I\\Modelo 3d\\assets\\"

# Dimensões da casa e jardim
altura_casa = 4
largura_x = 6
largura_y = 6
jardim_x = 3
jardim_y = 3


# Casa
draw_casa()

# Telhado
draw_telhado()

# Porta Principal
centro_porta_principal = (largura_x - jardim_x) / 2
x = largura_x
draw_cube_x(0, 2, 1, 0.01, centro_porta_principal, x, "marrom_claro.jpg", 0)

# Maçaneta (Porta Principal)
centro_macaneta = centro_porta_principal + 0.3
altura_macaneta = 0.9
x = largura_x
draw_cube_x(altura_macaneta, 0.3, 0.1, 0.03, centro_macaneta, x, "marrom_escuro.jpg", 0)

# Porta Jardim
centro_porta_jardim = largura_y - (jardim_y / 2)
x = largura_x - jardim_x
draw_cube_x(0, 2, 1, 0.01, centro_porta_jardim, x, "marrom_claro.jpg", 0)

# Maçaneta (Porta Jardim)
centro_macaneta = centro_porta_jardim + 0.3
altura_macaneta = 0.9
x = largura_x - jardim_x
draw_cube_x(altura_macaneta, 0.3, 0.1, 0.03, centro_macaneta, x, "marrom_escuro.jpg", 0)

# Janela Maior
draw_cube_x(1.5, 1.5, 4, 0, largura_y / 2, 0, "janela.jpg", -0.01)

# Janela Menor
centro_janela = (largura_x - jardim_x) / 2
y = largura_y
draw_cube_y(1.5, 1, 1, 0, centro_janela, y, "janela.jpg")
draw_cube_y(1.5, 1, 0.04, 0.001, centro_janela, y, "marrom_escuro.jpg") # Grades Verticais
draw_cube_y(2, 0.04, 1, 0.001, centro_janela, y, "marrom_escuro.jpg") # Grades Horizontais

# Janela de frente ao Jardim
centro_janela = largura_x - (jardim_x / 2)
y = largura_y - jardim_y
draw_cube_y(1.5, 1, 1, 0, centro_janela, y, "janela.jpg")
draw_cube_y(1.5, 1, 0.04, 0.001, centro_janela, y, "marrom_escuro.jpg") # Grades Verticais
draw_cube_y(2, 0.04, 1, 0.001, centro_janela, y, "marrom_escuro.jpg") # Grades Horizontais

#Jardim
altura_plano = 0
centro_jardim = largura_y / 2
x = 0
draw_cube_x(altura_plano, 0, largura_y, largura_x, centro_jardim, x, "verde.jpg", 0)

# Jardizinho
centro_jardizinho = largura_x - (jardim_x / 2)
y = largura_y - jardim_y
draw_cube_y(0, 0.5, jardim_x, 0.5, centro_jardizinho, y, "preto.jpg", 0)

# Terra do jardim
centro_jardizinho = largura_x - (jardim_x / 2)
y = largura_y - jardim_y + 0.125
draw_cube_y(0.51, 0, 2.5, 0.25, centro_jardizinho, y, "marrom.jpg", 0)