def imtf_algorithm(config_list, request_sequence):
    config = config_list.copy()
    total_cost = 0
    n = len(request_sequence)

    print("Inicial:", config)
    print("\nProcesando solicitudes con IMTF...\n")

    for idx, req in enumerate(request_sequence):
        pos = config.index(req)
        lookahead = request_sequence[idx + 1 : idx + pos]

        # Por defecto, asumimos que solo se accede sin mover
        if req in lookahead:
            cost = 2 * pos + 1  # acceso + movimiento
            config.pop(pos)
            config.insert(0, req)
            movimiento = "Se mueve al frente"
        else:
            cost = pos + 1  # solo acceso
            movimiento = "No se mueve"

        total_cost += cost

        print(
            f"Solicitud: {req}, Costo: {cost}, Configuración antes: {config} => {movimiento} → Configuración después: {config}"
        )

    print(f"\nCosto total de accesos (IMTF): {total_cost}")


config_list = [0, 1, 2, 3, 4]
request_sequence = [0] * 20
request_sequence_2 = [4, 3, 2, 1, 0] * 4

print("Ejecución del algoritmo IMTF para el mejor de los casos\n")
imtf_algorithm(config_list, request_sequence)

print("\nEjecución del algoritmo IMTF para el peor de los casos\n")
imtf_algorithm(config_list, request_sequence_2)
