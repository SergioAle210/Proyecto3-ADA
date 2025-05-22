def mtf_algorithm(config_list, request_sequence):
    config = config_list.copy()
    total_cost = 0

    print("Inicial:", config)
    print("\nProcesando solicitudes...\n")
    for req in request_sequence:
        index = config.index(req)
        cost = 2 * index + 1
        total_cost += cost

        print(
            f"Solicitud: {req}, Costo: {cost}, Configuración antes: {config}", end=" "
        )

        # Mover al frente
        config.pop(index)
        config.insert(0, req)

        print(f"=> Configuración después: {config}")

    print(f"\nCosto total de accesos: {total_cost}")


config_list = [0, 1, 2, 3, 4]
request_sequence = [0, 1, 2, 3, 4] * 4
request_seguence_2 = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
request_sequence_3 = [0] * 20
request_sequence_4 = [4, 3, 2, 1, 0] * 4
sequence_2s = [2] * 20
sequence_3s = [3] * 20

# Ejecutar el algoritmo
print("Ejecución del algoritmo MTF para el primer inciso\n")

mtf_algorithm(config_list, request_sequence)

print("\nEjecución del algoritmo MTF para el segundo inciso\n")

mtf_algorithm(config_list, request_seguence_2)

print("\nEjecución del algoritmo MTF para el tercer inciso\n")

mtf_algorithm(config_list, request_sequence_3)

print("\nEjecución del algoritmo MTF para el cuarto inciso\n")

mtf_algorithm(config_list, request_sequence_4)

print("\nEjecución del algoritmo MTF para el quinto inciso, secuencia de 2\n")

mtf_algorithm(config_list, sequence_2s)

print("\nEjecución del algoritmo MTF para el sexto inciso, secuencia de 3\n")

mtf_algorithm(config_list, sequence_3s)
