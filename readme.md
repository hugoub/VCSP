# Propuesta de modelo de programación entera para el problema de vehicle and crew scheduling con flota heterogénea de buses aplicado al transporte urbano de pasajeros.

El problema unificado de vehicle and crew scheduling con múltiples depósitos ha sido ampliamente estudiado en la literatura, sin embargo, sólo se ha considerado una flota homogénea de buses. En este artículo se propone un enfoque integrado para resolver los problemas de vehicle and crew scheduling con múltiples depósitos y flota heterogénea de buses. El enfoque propuesto está compuesto por un módulo de generación de turnos en función de las condiciones del problema. Los turnos deben generarse bajo restricciones de tipo organizacional y/o gubernamental, luego, son ingresados al modelo integrado de programación entera para obtener una solución. El problema de vehicle scheduling considera horarios punta para la elección de buses. La solución consiste en la asignación de un bus a cada viaje y en la asignación de una tripulación a cada bus. Con el fin de evaluar el modelo, se utiliza un conjunto de instancias reales de una empresa de transportes de la ciudad de Porto Alegre, Brasil. Se generaron 4 cantidades diferentes de turnos por cada instancia y el modelo se ejecuta durante 4 horas por cada una de las cantidades. El problema de programación matemática es modelado a través del software GAMS y resuelto mediante CPLEX. El modelo encuentra soluciones con un gap de hasta 5.8% en líneas de transporte con menos de 183 viajes. Los resultados obtenidos con instancias reales del problema sugieren que el modelo es apto para ser utilizado dentro de empresas de transporte y que la calidad de la solución depende de la cantidad de turnos generados y el tiempo de ejecución del modelo. 


# Paper

Se puede encontrar con el nombre:

```
Paper - Vehicle and Crew Scheduling Problem.pdf
```

### **Hugo Ubilla**