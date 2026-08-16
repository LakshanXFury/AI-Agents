flowchart TD
    START --> route

    route -->|confidence >= 0.6| answer
    route -->|confidence < 0.6| escalate

    answer --> END
    escalate --> END
 
 
                 START
                   |
                 route
                /     \
               /       \
      >= 0.6  /         \  < 0.6
             ↓           ↓
          answer       escalate
             |           |
             ↓           ↓
            END         END