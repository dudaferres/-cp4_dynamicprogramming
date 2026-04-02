def merge_sort(arr):
    # Caso base: se a lista tem 1 ou 0 elementos, já está ordenada
    if len(arr) <= 1:
        return arr

    # Divide a lista ao meio
    mid = len(arr) // 2

    # Recursão: ordena a metade esquerda
    left = merge_sort(arr[:mid])

    # Recursão: ordena a metade direita
    right = merge_sort(arr[mid:])

    # Combina as metades ordenadas
    return merge(left, right)


def merge(left, right):
    # Lista para armazenar o resultado mesclado
    result = []

    # Índices para percorrer as listas esquerda e direita
    i = j = 0

    # Enquanto houver elementos em ambas as listas
    while i < len(left) and j < len(right):
        # Compara os elementos atuais e adiciona o menor à lista resultante
        if left[i] < right[j]:
            result.append(left[i])
            i += 1  # Avança na lista esquerda
        else:
            result.append(right[j])
            j += 1  # Avança na lista direita

    # Adiciona os elementos restantes da lista esquerda (se houver)
    result.extend(left[i:])

    # Adiciona os elementos restantes da lista direita (se houver)
    result.extend(right[j:])

    # Retorna a lista mesclada e ordenada
    return result