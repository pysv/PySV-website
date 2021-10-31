import uuid
import python_avatars as pa


if __name__ == "__main__":

    random_avatar_3 = pa.Avatar(
        style=pa.AvatarStyle.TRANSPARENT,
        background_color=pa.BackgroundColor.pick_random(),
        top=pa.HairType.pick_random(),
        eyebrows=pa.EyebrowType.DEFAULT_NATURAL,
        eyes=pa.EyeType.DEFAULT,
        nose=pa.NoseType.pick_random(),
        mouth=pa.MouthType.SMILE,
        facial_hair=pa.FacialHairType.pick_random(favor=pa.FacialHairType.NONE),  # favour putting one, i.e. less f/d
        # You can use hex colors on any color attribute...
        skin_color=pa.SkinColor.pick_random(),
        # Or you can use the colors provided by the library
        hair_color=pa.HairColor.pick_random(),
        accessory=pa.AccessoryType.NONE,
        clothing=pa.ClothingType.pick_random(),
        shirt_text='PySV',
    ).render(f"avatars/avatar_{uuid.uuid4().hex[:6]}.svg")