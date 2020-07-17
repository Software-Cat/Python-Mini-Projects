def distance_of_storm(deltaT):
    """
    Calculate the distance a thundersotrm is away from the observer
    
    Speed of lightning: 299792458 m/s
    Speed of thunder: 343 m/s
    difference in speed: 229792115 m/s
    """
    TheDifferenceInPos = deltaT * 343
