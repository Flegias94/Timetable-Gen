from models.entities import StudentGroup


def load_student_groups():
    student_groups = [
        StudentGroup(id="AF1G1", specialization="AF", year=1, size=21, course_ids=[]),
        StudentGroup(id="AF1G2", specialization="AF", year=1, size=21, course_ids=[]),
        StudentGroup(id="AF1G3", specialization="AF", year=1, size=21, course_ids=[]),
        # ⚠️ Adjusted from 4 to 5 semigroups to satisfy max 15 constraint,
        StudentGroup(id="af1sg1", specialization="AF", year=1, size=13, course_ids=[]),
        StudentGroup(id="af1sg2", specialization="AF", year=1, size=13, course_ids=[]),
        StudentGroup(id="af1sg3", specialization="AF", year=1, size=13, course_ids=[]),
        StudentGroup(id="af1sg4", specialization="AF", year=1, size=13, course_ids=[]),
        StudentGroup(id="af1sg5", specialization="AF", year=1, size=13, course_ids=[]),
        StudentGroup(id="AF2G1", specialization="AF", year=2, size=19, course_ids=[]),
        StudentGroup(id="AF2G2", specialization="AF", year=2, size=19, course_ids=[]),
        StudentGroup(id="af2sg1", specialization="AF", year=2, size=13, course_ids=[]),
        StudentGroup(id="af2sg2", specialization="AF", year=2, size=13, course_ids=[]),
        StudentGroup(id="af2sg3", specialization="AF", year=2, size=13, course_ids=[]),
        StudentGroup(id="IE3G1", specialization="IE", year=3, size=17, course_ids=[]),
        StudentGroup(id="IE3G2", specialization="IE", year=3, size=17, course_ids=[]),
        # ⚠️ Adjusted from 2 to 3 semigroups to satisfy max 15 constraint,
        StudentGroup(id="ie3sg1", specialization="IE", year=3, size=12, course_ids=[]),
        StudentGroup(id="ie3sg2", specialization="IE", year=3, size=12, course_ids=[]),
        StudentGroup(id="ie3sg3", specialization="IE", year=3, size=12, course_ids=[]),
        StudentGroup(id="IE2G1", specialization="IE", year=2, size=20, course_ids=[]),
        StudentGroup(id="IE2G2", specialization="IE", year=2, size=20, course_ids=[]),
        StudentGroup(id="ie2sg1", specialization="IE", year=2, size=14, course_ids=[]),
        StudentGroup(id="ie2sg2", specialization="IE", year=2, size=14, course_ids=[]),
        StudentGroup(id="ie2sg3", specialization="IE", year=2, size=14, course_ids=[]),
        StudentGroup(id="IE1G1", specialization="IE", year=1, size=21, course_ids=[]),
        StudentGroup(id="IE1G2", specialization="IE", year=1, size=21, course_ids=[]),
        StudentGroup(id="ie1sg1", specialization="IE", year=1, size=14, course_ids=[]),
        StudentGroup(id="ie1sg2", specialization="IE", year=1, size=14, course_ids=[]),
        StudentGroup(id="ie1sg3", specialization="IE", year=1, size=14, course_ids=[]),
        StudentGroup(id="AF3G1", specialization="AF", year=3, size=17, course_ids=[]),
        StudentGroup(id="AF3G2", specialization="AF", year=3, size=17, course_ids=[]),
        # ⚠️ Adjusted from 2 to 3 semigroups to satisfy max 15 constraint,
        StudentGroup(id="af3sg1", specialization="AF", year=3, size=12, course_ids=[]),
        StudentGroup(id="af3sg2", specialization="AF", year=3, size=12, course_ids=[]),
        StudentGroup(id="af3sg3", specialization="AF", year=3, size=12, course_ids=[]),
        StudentGroup(id="AI1G1", specialization="AI", year=1, size=20, course_ids=[]),
        StudentGroup(id="AI1G2", specialization="AI", year=1, size=20, course_ids=[]),
        StudentGroup(id="ai1sg1", specialization="AI", year=1, size=13, course_ids=[]),
        StudentGroup(id="ai1sg2", specialization="AI", year=1, size=13, course_ids=[]),
        StudentGroup(id="ai1sg3", specialization="AI", year=1, size=13, course_ids=[]),
        StudentGroup(id="AI2G1", specialization="AI", year=2, size=19, course_ids=[]),
        StudentGroup(id="AI2G2", specialization="AI", year=2, size=19, course_ids=[]),
        StudentGroup(id="ai2sg1", specialization="AI", year=2, size=13, course_ids=[]),
        StudentGroup(id="ai2sg2", specialization="AI", year=2, size=13, course_ids=[]),
        StudentGroup(id="ai2sg3", specialization="AI", year=2, size=13, course_ids=[]),
        StudentGroup(id="AI3G1", specialization="AI", year=3, size=16, course_ids=[]),
        StudentGroup(id="AI3G2", specialization="AI", year=3, size=16, course_ids=[]),
        # ⚠️ Adjusted from 2 to 3 semigroups to satisfy max 15 constraint,
        StudentGroup(id="ai3sg1", specialization="AI", year=3, size=11, course_ids=[]),
        StudentGroup(id="ai3sg2", specialization="AI", year=3, size=11, course_ids=[]),
        StudentGroup(id="ai3sg3", specialization="AI", year=3, size=11, course_ids=[]),
        StudentGroup(id="AMA1G1", specialization="AMA", year=1, size=29, course_ids=[]),
        StudentGroup(
            id="ama1sg1", specialization="AMA", year=1, size=15, course_ids=[]
        ),
        StudentGroup(
            id="ama1sg2", specialization="AMA", year=1, size=15, course_ids=[]
        ),
        StudentGroup(id="AMA2G1", specialization="AMA", year=2, size=27, course_ids=[]),
        StudentGroup(
            id="ama2sg1", specialization="AMA", year=2, size=14, course_ids=[]
        ),
        StudentGroup(
            id="ama2sg2", specialization="AMA", year=2, size=14, course_ids=[]
        ),
        StudentGroup(id="AMA3G1", specialization="AMA", year=3, size=28, course_ids=[]),
        StudentGroup(
            id="ama3sg1", specialization="AMA", year=3, size=14, course_ids=[]
        ),
        StudentGroup(
            id="ama3sg2", specialization="AMA", year=3, size=14, course_ids=[]
        ),
        StudentGroup(id="CIG1G1", specialization="CIG", year=1, size=28, course_ids=[]),
        StudentGroup(id="CIG1G2", specialization="CIG", year=1, size=28, course_ids=[]),
        StudentGroup(id="CIG1G3", specialization="CIG", year=1, size=28, course_ids=[]),
        StudentGroup(id="CIG1G4", specialization="CIG", year=1, size=28, course_ids=[]),
        # ⚠️ Adjusted from 7 to 8 semigroups to satisfy max 15 constraint,
        StudentGroup(
            id="cig1sg1", specialization="CIG", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig1sg2", specialization="CIG", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig1sg3", specialization="CIG", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig1sg4", specialization="CIG", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig1sg5", specialization="CIG", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig1sg6", specialization="CIG", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig1sg7", specialization="CIG", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig1sg8", specialization="CIG", year=1, size=14, course_ids=[]
        ),
        StudentGroup(id="CIG2G1", specialization="CIG", year=2, size=31, course_ids=[]),
        StudentGroup(id="CIG2G2", specialization="CIG", year=2, size=31, course_ids=[]),
        StudentGroup(id="CIG2G3", specialization="CIG", year=2, size=31, course_ids=[]),
        # ⚠️ Adjusted from 6 to 7 semigroups to satisfy max 15 constraint,
        StudentGroup(
            id="cig2sg1", specialization="CIG", year=2, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig2sg2", specialization="CIG", year=2, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig2sg3", specialization="CIG", year=2, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig2sg4", specialization="CIG", year=2, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig2sg5", specialization="CIG", year=2, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig2sg6", specialization="CIG", year=2, size=14, course_ids=[]
        ),
        StudentGroup(
            id="cig2sg7", specialization="CIG", year=2, size=14, course_ids=[]
        ),
        StudentGroup(id="CIG3G1", specialization="CIG", year=3, size=24, course_ids=[]),
        StudentGroup(id="CIG3G2", specialization="CIG", year=3, size=24, course_ids=[]),
        StudentGroup(id="CIG3G3", specialization="CIG", year=3, size=24, course_ids=[]),
        # ⚠️ Adjusted from 4 to 5 semigroups to satisfy max 15 constraint,
        StudentGroup(
            id="cig3sg1", specialization="CIG", year=3, size=15, course_ids=[]
        ),
        StudentGroup(
            id="cig3sg2", specialization="CIG", year=3, size=15, course_ids=[]
        ),
        StudentGroup(
            id="cig3sg3", specialization="CIG", year=3, size=15, course_ids=[]
        ),
        StudentGroup(
            id="cig3sg4", specialization="CIG", year=3, size=15, course_ids=[]
        ),
        StudentGroup(
            id="cig3sg5", specialization="CIG", year=3, size=15, course_ids=[]
        ),
        StudentGroup(
            id="ECTS1G1", specialization="ECTS", year=1, size=22, course_ids=[]
        ),
        StudentGroup(
            id="ECTS1G2", specialization="ECTS", year=1, size=22, course_ids=[]
        ),
        StudentGroup(
            id="ECTS1G3", specialization="ECTS", year=1, size=22, course_ids=[]
        ),
        # ⚠️ Adjusted from 4 to 5 semigroups to satisfy max 15 constraint,
        StudentGroup(
            id="ects1sg1", specialization="ECTS", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="ects1sg2", specialization="ECTS", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="ects1sg3", specialization="ECTS", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="ects1sg4", specialization="ECTS", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="ects1sg5", specialization="ECTS", year=1, size=14, course_ids=[]
        ),
        StudentGroup(
            id="ECTS2G1", specialization="ECTS", year=2, size=24, course_ids=[]
        ),
        StudentGroup(
            id="ECTS2G2", specialization="ECTS", year=2, size=24, course_ids=[]
        ),
        # ⚠️ Adjusted from 3 to 4 semigroups to satisfy max 15 constraint,
        StudentGroup(
            id="ects2sg1", specialization="ECTS", year=2, size=12, course_ids=[]
        ),
        StudentGroup(
            id="ects2sg2", specialization="ECTS", year=2, size=12, course_ids=[]
        ),
        StudentGroup(
            id="ects2sg3", specialization="ECTS", year=2, size=12, course_ids=[]
        ),
        StudentGroup(
            id="ects2sg4", specialization="ECTS", year=2, size=12, course_ids=[]
        ),
        StudentGroup(
            id="ECTS3G1", specialization="ECTS", year=3, size=23, course_ids=[]
        ),
        StudentGroup(
            id="ECTS3G2", specialization="ECTS", year=3, size=23, course_ids=[]
        ),
        # ⚠️ Adjusted from 3 to 4 semigroups to satisfy max 15 constraint,
        StudentGroup(
            id="ects3sg1", specialization="ECTS", year=3, size=12, course_ids=[]
        ),
        StudentGroup(
            id="ects3sg2", specialization="ECTS", year=3, size=12, course_ids=[]
        ),
        StudentGroup(
            id="ects3sg3", specialization="ECTS", year=3, size=12, course_ids=[]
        ),
        StudentGroup(
            id="ects3sg4", specialization="ECTS", year=3, size=12, course_ids=[]
        ),
        StudentGroup(
            id="EGCE1G1", specialization="EGCE", year=1, size=24, course_ids=[]
        ),
        StudentGroup(
            id="egce1sg1", specialization="EGCE", year=1, size=12, course_ids=[]
        ),
        StudentGroup(
            id="egce1sg2", specialization="EGCE", year=1, size=12, course_ids=[]
        ),
        StudentGroup(
            id="EGCE2G1", specialization="EGCE", year=2, size=18, course_ids=[]
        ),
        StudentGroup(
            id="EGCE2G2", specialization="EGCE", year=2, size=18, course_ids=[]
        ),
        # ⚠️ Adjusted from 2 to 3 semigroups to satisfy max 15 constraint,
        StudentGroup(
            id="egce2sg1", specialization="EGCE", year=2, size=12, course_ids=[]
        ),
        StudentGroup(
            id="egce2sg2", specialization="EGCE", year=2, size=12, course_ids=[]
        ),
        StudentGroup(
            id="egce2sg3", specialization="EGCE", year=2, size=12, course_ids=[]
        ),
        StudentGroup(
            id="EGCE3G1", specialization="EGCE", year=3, size=19, course_ids=[]
        ),
        StudentGroup(
            id="egce3sg1", specialization="EGCE", year=3, size=10, course_ids=[]
        ),
        StudentGroup(
            id="egce3sg2", specialization="EGCE", year=3, size=10, course_ids=[]
        ),
        StudentGroup(id="FB1G1", specialization="FB", year=1, size=29, course_ids=[]),
        StudentGroup(id="FB1G2", specialization="FB", year=1, size=29, course_ids=[]),
        StudentGroup(id="fb1sg1", specialization="FB", year=1, size=15, course_ids=[]),
        StudentGroup(id="fb1sg2", specialization="FB", year=1, size=15, course_ids=[]),
        StudentGroup(id="fb1sg3", specialization="FB", year=1, size=15, course_ids=[]),
        StudentGroup(id="fb1sg4", specialization="FB", year=1, size=15, course_ids=[]),
        StudentGroup(id="FB2G1", specialization="FB", year=2, size=23, course_ids=[]),
        StudentGroup(id="FB2G2", specialization="FB", year=2, size=23, course_ids=[]),
        StudentGroup(id="fb2sg1", specialization="FB", year=2, size=15, course_ids=[]),
        StudentGroup(id="fb2sg2", specialization="FB", year=2, size=15, course_ids=[]),
        StudentGroup(id="fb2sg3", specialization="FB", year=2, size=15, course_ids=[]),
        StudentGroup(id="FB3G1", specialization="FB", year=3, size=20, course_ids=[]),
        StudentGroup(id="FB3G2", specialization="FB", year=3, size=20, course_ids=[]),
        # ⚠️ Adjusted from 2 to 3 semigroups to satisfy max 15 constraint,
        StudentGroup(id="fb3sg1", specialization="FB", year=3, size=14, course_ids=[]),
        StudentGroup(id="fb3sg2", specialization="FB", year=3, size=14, course_ids=[]),
        StudentGroup(id="fb3sg3", specialization="FB", year=3, size=14, course_ids=[]),
        StudentGroup(id="MNG1G1", specialization="MNG", year=1, size=23, course_ids=[]),
        StudentGroup(id="MNG1G2", specialization="MNG", year=1, size=23, course_ids=[]),
        # ⚠️ Adjusted from 3 to 4 semigroups to satisfy max 15 constraint,
        StudentGroup(
            id="mng1sg1", specialization="MNG", year=1, size=12, course_ids=[]
        ),
        StudentGroup(
            id="mng1sg2", specialization="MNG", year=1, size=12, course_ids=[]
        ),
        StudentGroup(
            id="mng1sg3", specialization="MNG", year=1, size=12, course_ids=[]
        ),
        StudentGroup(
            id="mng1sg4", specialization="MNG", year=1, size=12, course_ids=[]
        ),
        StudentGroup(id="MNG2G1", specialization="MNG", year=2, size=30, course_ids=[]),
        StudentGroup(
            id="mng2sg1", specialization="MNG", year=2, size=15, course_ids=[]
        ),
        StudentGroup(
            id="mng2sg2", specialization="MNG", year=2, size=15, course_ids=[]
        ),
        StudentGroup(id="MNG3G1", specialization="MNG", year=3, size=18, course_ids=[]),
        StudentGroup(id="MNG3G2", specialization="MNG", year=3, size=18, course_ids=[]),
        # ⚠️ Adjusted from 2 to 3 semigroups to satisfy max 15 constraint,
        StudentGroup(
            id="mng3sg1", specialization="MNG", year=3, size=12, course_ids=[]
        ),
        StudentGroup(
            id="mng3sg2", specialization="MNG", year=3, size=12, course_ids=[]
        ),
        StudentGroup(
            id="mng3sg3", specialization="MNG", year=3, size=12, course_ids=[]
        ),
    ]
    return student_groups
