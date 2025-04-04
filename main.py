from pprint import pprint

from src.erewhon_astro import PlateSolve

def main():
    plate_solve = PlateSolve()
    local_solution = plate_solve.solve("test_images/test_image.jpg",
                                 local_solve=True)
    net_solution = plate_solve.solve("test_images/test_image.jpg",
                                 local_solve=False)

    pprint(local_solution.annotations)
    pprint(net_solution.annotations)

if __name__ == "__main__":
    main()
