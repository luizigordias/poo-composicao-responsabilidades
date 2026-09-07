# Diagrama da estação meteorológica

Complete as relações, multiplicidades, atributos e operações que faltam. O diagrama final deve corresponder ao código entregue.

```mermaid
classDiagram
    class SensorTemperatura {
        -valor_: double
        +atualizar(valor: double) bool
        +valor() double
    }
    
    class AlarmeTermico {
        -ligado_: bool
        +avaliar(temperatura: double) void
        +estaLigado() bool
    }
    
    class EstacaoMeteorologica {
        -sensor_: SensorTemperatura
        -alarme_: AlarmeTermico
        +EstacaoMeteorologica(tag: string, temperaturaInicial: double)
        +registrarTemperatura(temperatura: double) bool
        +temperatura() double
        +alarmeLigado() bool
    }
    
    %% Composição e multiplicidades
    EstacaoMeteorologica *-- "1" SensorTemperatura : contém
    EstacaoMeteorologica *-- "1" AlarmeTermico : contém
```
