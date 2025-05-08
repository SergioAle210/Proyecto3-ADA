def imtf_algorithm(config_list, request_sequence):
    config = config_list.copy()
    total_cost = 0
    n = len(request_sequence)

    print("Inicial:", config)
    print("\nProcesando solicitudes con IMTF...\n")

    for idx, req in enumerate(request_sequence):
        pos = config.index(req)
        cost = pos + 1
        total_cost += cost

        print(
            f"Solicitud: {req}, Costo: {cost}, Configuración antes: {config}", end=" "
        )

        # Condición de movimiento según IMTF
        lookahead = request_sequence[idx + 1 : idx + pos]
        if req in lookahead:
            config.pop(pos)
            config.insert(0, req)
            print(f"=> Se mueve al frente → Configuración después: {config}")
        else:
            print(f"=> No se mueve → Configuración después: {config}")

    print(f"\nCosto total de accesos (IMTF): {total_cost}")


config_list = [0, 1, 2, 3, 4]
request_sequence = [0, 1, 2, 3, 4] * 4
request_sequence_2 = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]

print("Ejecución del algoritmo IMTF para el primer inciso\n")
imtf_algorithm(config_list, request_sequence)

print("\nEjecución del algoritmo IMTF para el segundo inciso\n")
imtf_algorithm(config_list, request_sequence_2)
