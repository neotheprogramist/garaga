p=0x1a0111ea397fe69a4b1ba7b6434bacd764774b84f38512bf6730d2a0f6b0f6241eabfffeb153ffffb9feffffffffaaab
assert p == 4002409555221667393417789825735904156556882819939007885332058136124031650490837864442687629129015664037894272559787
b64 = 2**64
two_inv = 1730508156817200468 + 9606178027640717313*b64 + 7150789853162776431*b64**2 + 7936136305760253186*b64**3 + 15245073033536294050*b64**4 + 1728177566264616342*b64**5
BASE=2**96
DEGREE=3


def split(x, degree=DEGREE, base=BASE):
    coeffs = []
    for n in range(degree, 0, -1):
        q, r = divmod(x, base ** n)
        coeffs.append(q)
        x = r
    coeffs.append(x)
    return coeffs[::-1]


p1 = (4, 1630892974828014537729259858097113969650871260980656934049590190201941782487224876496582135785777461178964897591404)
p2 = ([2, 0], [188995492400578496451910581292546059920654572609832469388872107051048741028892423057992033888655218419282460458611, 434381874456081807472298918693162486998243066160460423017297172308631992219110538691921044767658182807847155297615])
print(p1)
print(p2)

l=[split(p2[0][0]),split(p2[0][1]),split(p2[1][0]),split(p2[1][1])]
print(l)

# Drand sample data 
pk_g2 = (2145611392864255159976058193707798019683871237740924092868198719624192115446304628388726536638189318698326690875998, 
         110857442005619299284728452020835925565209931756337496598513277468603514687751181984009099979594460331023913803661, 
         1434254128448074948435371238907902528224898884378856995830267731418682609636468653915292088321706382884080263265154,
        2423758172102577229014107694432354685978307565965474922546916380817758084955253559753459407647904482991347476289049)

message_G1_round_1 = (3338652663552600328513890811770152635754069895120181533752182037935744376986083745943138570800650991303107023886527, 
                      1854371379838501232711008369216482603147910350737957495174982112162169472602772231304024719417229260292776537455662)
sigma_G1_round_1 = (3273600169547635740816701851659619499431544873765376282654705539451685781348277316934196131615542531240307808626640, 
                    1866496026253639371864984433178947388482749394163726970403413407540822630091645787929290599630468890819582357156796)

g2_drand = (352701069587466618187139116011060144890029952792775240219908644239793785735715026873347600343865175952761926303160,
            3059144344244213709971259814753781636986470325476647558659373206291635324768958432433509563104347017837885763365758,
            1985150602287291935568054521177171638300868978215655730859378665066344726373823718423869104263333984641494340347905,
            927553665492332455747201965776037880757740193453592970025027978793976877002675564980949289727957565575433344219582)
# check e(sigma, g2) == e(message, pk_g2)