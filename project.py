def mtf_algorithm(config_list, request_sequence):
    config = config_list.copy()
    total_cost = 0

    print("Inicial:", config)
    print("\nProcesando solicitudes...\n")
    for req in request_sequence:
        index = config.index(req)
        cost = index + 1
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

# Ejecutar el algoritmo
mtf_algorithm(config_list, request_sequence)
