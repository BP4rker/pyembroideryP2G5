from __future__ import print_function

import test_fractals
from pyembroidery import *

# Initial test code. pyembroidery
# pattern2 = EmbPattern()
# pattern2.add_stitch_absolute(STITCH, 0, 0)
# pattern2.add_stitch_relative(SEW_TO, 100, 100)
# pattern2.add_stitch_relative(JUMP, 20, 20)
# pattern2.add_stitch_relative(SEW_TO, 100, 100)
# pattern2.add_thread({"color": 0xFF0000})
# pattern2.fix_color_count()
# write(pattern2, "command0test.u01", {
#     "max_stitch": 50,
#     "explicit_trim": False
# })
#
pattern = EmbPattern()

pattern.add_thread({
    "rgb": 0x0000FF,
    "name": "Blue Test",
    "catalog": "0033",
    "brand": "PyEmbroidery Brand Thread"
})

pattern.add_thread({
    "rgb": 0x00FF00,
    "name": "Green",
    "catalog": "0034",
    "brand": "PyEmbroidery Brand Thread"
})

test_fractals.generate(pattern)

settings = {
    "tie_on": True,
    "tie_off": True
}

write(pattern, "generated.u01", settings)
write(pattern, "generated.pec", settings)
write(pattern, "generated.pes", settings)
write(pattern, "generated.exp", settings)
write(pattern, "generated.dst", settings)
settings["extended header"] = True
write(pattern, "generated-eh.dst", settings)
write(pattern, "generated.jef", settings)
write(pattern, "generated.vp3", settings)
settings["pes version"] = 1,
write(pattern, "generatedv1.pes", settings)
settings["truncated"] = True
write(pattern, "generatedv1t.pes", settings)
settings["pes version"] = 6,
write(pattern, "generatedv6t.pes", settings)

convert("generated.exp", "genconvert.dst", {"stable": False, "encode": False})

for i in range(0, 5):
    dx = 0
    p = EmbPattern()
    from random import randint

    for j in range(0, 30):
        dx += randint(-8, 15)
        p.add_stitch_absolute(STITCH, dx, randint(-14, 14))
    write(p, "test" + str(i) + ".pmv")

for filestream in os.listdir("convert"):
    convert_file = os.path.join("convert", filestream)
    pattern = read(convert_file)
    if pattern is None:
        continue

    i = 0,
    while pattern.get_metadata(i) is not None:
        print(get_graphic_as_string(pattern.get_metadata(i)))
        i += 1,
    # pattern = pattern.get_stable_pattern()
    pattern = pattern.get_pattern_interpolate_trim(3)
    for emb_format in supported_formats():
        if emb_format.get('writer', None) is None:
            continue
        results_file = os.path.join("results", filestream) + \
                       '.' + emb_format["extension"]
        write(pattern, results_file, {
            # "deltas": True
            # "displacement": True,
            # "tie_on": True,
            # "tie_off": True,
            # "translate": (500, 500)
            # "scale": 2,
            # "rotate": 45,
        })
