import math
import tempfile
import unittest
from pathlib import Path

import rock_lab as lab


def row(**values):
    return dict.fromkeys(lab.FIELDS, "") | {"pile": "A", "rock_id": "A01", "repeat": "1"} | values


class LabTests(unittest.TestCase):
    def test_dimensions_and_units(self):
        out = lab.measure(row(length_mm="60", width_mm="40", thickness_mm="30"))
        self.assertAlmostEqual(out["ellipsoid_cm3"][0], 37.699111843)
        self.assertEqual(out["axis_ratio"][0], .5)
        self.assertNotIn("wadell", out)

    def test_displacement_density(self):
        out = lab.measure(row(dry_mass_g="96", initial_ml="200", submerged_ml="240",
                              volume_method="water-accessible"))
        self.assertEqual(out["displacement_cm3"], (40, "water-accessible"))
        self.assertEqual(out["density_g_cm3"], (2.4, "water-accessible"))

    def test_wadell_sphere(self):
        out = lab.measure(row(shape_volume_cm3=str(4*math.pi/3), area_cm2=str(4*math.pi),
                              shape_boundary="known sphere"))
        self.assertAlmostEqual(out["wadell"][0], 1)

    def test_rejects_impossible_inputs(self):
        for bad in (row(length_mm="nan"), row(initial_ml="50", submerged_ml="40", volume_method="direct"),
                    row(shape_volume_cm3="12", area_cm2="1", shape_boundary="same"),
                    row(shape_volume_cm3="12", area_cm2="10"), row(initial_ml="50")):
            with self.assertRaises(ValueError):
                lab.measure(bad)

    def test_repeats_are_grouped_not_counted_as_rocks(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "rows.csv"
            inputs = [row(length_mm="60"), row(length_mm="61", repeat="2")]
            lab.write_rows(p, lab.FIELDS, [r.values() for r in inputs])
            values, known = lab.read_measurements(p)
            self.assertEqual(known, {("A", "A01")})
            self.assertEqual(values["A", "A01", "length_mm", ""], [60, 61])

    def test_equal_means_unequal_spread(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "regions.csv"
            lab.write_rows(p, lab.REGION_FIELDS,
                           (("A", rock, "long-axis", i, 10, occupied)
                            for rock, v in (("A01", [9,9,9,9]), ("A02", [10,10,10,6]))
                            for i, occupied in enumerate(v, 1)))
            result = dict(lab.regional_values(p, {("A","A01"), ("A","A02")}))
            scheme = "long-axis; k=4"
            self.assertAlmostEqual(result["A","A01","void_mean_pp",scheme][0], 10)
            self.assertAlmostEqual(result["A","A02","void_mean_pp",scheme][0], 10)
            self.assertAlmostEqual(result["A","A01","void_sd_pp",scheme][0], 0)
            self.assertAlmostEqual(result["A","A02","void_sd_pp",scheme][0], math.sqrt(300))


if __name__ == "__main__":
    unittest.main()
