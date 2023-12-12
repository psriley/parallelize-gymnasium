class Lander():
    crashed = False
    legs
    body

    def __init__(self, initial_x, initial_y) -> None:
        create_body()
        create_legs()
        self.world.CreateDynamicBody(
                position=(initial_x, initial_y),
                angle=0.0,
                fixtures=fixtureDef(
                    shape=polygonShape(
                        vertices=[(x / SCALE, y / SCALE) for x, y in LANDER_POLY]
                    ),
                    density=5.0,
                    friction=0.1,
                    categoryBits=0x0010,
                    maskBits=0x001,  # collide only with ground
                    restitution=0.0,
                ),
            )

