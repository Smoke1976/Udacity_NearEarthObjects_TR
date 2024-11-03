"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional),
    diameterin kilometers (optional - sometimes unknown), and whether it's
    marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation='', name=None, diameter=None,
                 hazardous=False):
        """Create a new `NearEarthObject`.

        :param designation: designation of NEO given by NASA (str)
        :param name: name of NEO given by NASA (str)
        :param diameter: diameter of NEO in km (float)
        :param hazardous: True if NEO is hazardous to Earth (bool)
        """
        self.designation = designation if designation is not None else ''
        self.name = name if name is not None else None
        if diameter is not None and diameter != '':
            self.diameter = float(diameter)
        else:
            self.diameter = float('nan')
        self.hazardous = hazardous if hazardous is not None else False
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return str(self.designation) + ' (' + str(self.name) + ')'

    def __str__(self):
        """Return `str(self)`."""
        if {self.hazardous}:
            return f"A NearEarthObject {self.fullname} with a "\
                f"diameter of {self.diameter} km is HAZARDOUS!"
        else:
            return f"A NearEarthObject {self.fullname} with a "\
                f"diameter of {self.diameter} km is NOT hazardous!"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string of this object."""
        return (
            f"NearEarthObject(designation={self.designation!r}, "
            f"name={self.name!r}, diameter={self.diameter:.3f}, "
            f"hazardous={self.hazardous!r})"
        )


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach
    to Earth, such as the date and time (in UTC) of closest approach, the
    nominal approach distance in astronomical units, and the relative approach
    velocity in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation='', cad_time=None, distance=0.0,
                 velocity=0.0, neo=None):
        """Create a new `CloseApproach`.

        :param designation: The designation of the NEO given by NASA
        :param cad_time: date of the approach in YYYY-MMM-DD hh:mm Format
        :param distance: the distance of the approach
        :param velocity: the relative velocity of the approach
        """
        self._designation = designation if designation is not None else ''
        self.time = cd_to_datetime(cad_time) if cad_time is not None else None
        self.distance = distance if distance is not None \
            and isinstance(distance, float) else 0.0
        self.velocity = velocity if velocity is not None \
            and isinstance(velocity, float) else 0.0
        self.neo = neo if neo is not None else None

    @property
    def time_str(self):
        """Return a formatted output of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default
        representation includes seconds - significant figures that don't
        exist in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return (
            f"A CloseApproach for a {self.neo.fullname} happens or happened at"
            f" {datetime_to_str(self.time)} with a velocity of {self.velocity}"
            f" km/s at a distance of {self.distance} au!"
        )

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string of this object."""
        return (
            f"CloseApproach(time={self.time_str!r}, "
            f"distance={self.distance:.2f}, "
            f"velocity={self.velocity:.2f}, neo={self.neo!r})"
        )
