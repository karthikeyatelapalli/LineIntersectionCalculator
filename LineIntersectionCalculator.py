# Intersecting Points(with classes)
 
'''
Description: The LinearEquations class in this Python program is defined to determine the intersection_points of two lines given four points. If the lines do meet,
the intersection point is calculated using Cramer's rule using the coefficients of the lines in the form ax + by = c. The user is prompted to
enter four points, and the application displays the equation of the two lines and, if they cross, the point of intersection.

'''
# Define the LinearEquations class, which accepts four input points.
class LinearEquations:
    def __init__(self, point1, point2, point3, point4):
        # It stores the four points as private variables
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3
        self.__point4 = point4
    
    def obtain_the_cofficients(self):
        # Extract the four points' x and y coordinates.
        # determines the coefficients of the lines in the form of 'ax + by = c'.
        self.__a = self.__point1[1] - self.__point2[1]
        self.__b = -(self.__point1[0] - self.__point2[0])
        self.__c = self.__point3[1] - self.__point4[1]
        self.__d = -(self.__point3[0] - self.__point4[0])
        self.__e = (self.__point1[1] - self.__point2[1])*self.__point1[0] - (self.__point1[0] - self.__point2[0])*self.__point1[1]
        self.__f = (self.__point3[1] - self.__point4[1])*self.__point3[0] - (self.__point3[0] - self.__point4[0])*self.__point3[1]

        # Returns coefficients.
        return self.__a, self.__b, self.__c, self.__d, self.__e, self.__f

    def __str__(self):
        # It gets the coefficients.
        a , b, c, d, e, f = self.obtain_the_cofficients()

        # Returns the equations of the lines as formatted string.
        string = f"""The equation of the first line (with points {self.__point1} and {self.__point2}) is:
{a}x + {b}y = {e}
The equation of the second line (with points {self.__point3} and {self.__point4}) is:
{c}x + {d}y = {f}"""
        
        return string
    
    def boolean(self):
        # It gets the coefficients.
        a , b, c, d, e, f = self.obtain_the_cofficients()

        # Check if the two lines intersect using Cramer's rule.
        if a*d - b*c !=0:
            return True
        else:
            return False
        
    def intersection_points(self):
        # It gets the coefficients.
        a , b, c, d, e, f = self.obtain_the_cofficients()

        # Determine intersection points point by following Cramer's rule.
        x = (e*d - b*f) / (a*d - b*c)
        y = (a*f - e*c) / (a*d - b*c)

        # Return the intersection points point as formatted string.
        return f"({x:.1f}, {y:.1f})"
    

def main():
    # Asks the user to enter the four points.
    point1 = tuple(float(i) for i in input("Enter the x and y coordinates of point1: ").split())
    point2 = tuple(float(i) for i in input("Enter the x and y coordinates of point2: ").split())
    point3 = tuple(float(i) for i in input("Enter the x and y coordinates of point3: ").split())
    point4 = tuple(float(i) for i in input("Enter the x and y coordinates of point4: ").split())

    # Creates a LinearEquations object with that four points.
    linearequations_object = LinearEquations(point1, point2, point3, point4)

    # This prints the equations of the two lines.
    print(linearequations_object)
    print()

    # This checks if the two lines intersect, and if they do intersect it prints the intersection point.
    if linearequations_object.boolean():
        print(f"The intersecting point is: {linearequations_object.intersection_points()}.")
    else:
        print("The two lines do not intersect.")

if __name__ == "__main__":
    main()
