"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .business import BusinessFields
    from .collaborativeadssharesettings import CollaborativeAdsShareSettingsFields
    from .commercemerchantsettings import CommerceMerchantSettingsFields
    from .productcatalogimagesettings import ProductCatalogImageSettingsFields
    from .storecatalogsettings import StoreCatalogSettingsFields
    from .user import UserFields


class productcatalogpricing_variables_batch_standard_enum_param(str, Enum):
    """productcatalogpricing_variables_batch_standard_enum_param enum values."""

    google = "google"


class productcatalogagencies_permitted_tasks_enum_param(str, Enum):
    """productcatalogagencies_permitted_tasks_enum_param enum values."""

    AA_ANALYZE = "AA_ANALYZE"
    ADVERTISE = "ADVERTISE"
    MANAGE = "MANAGE"
    MANAGE_AR = "MANAGE_AR"


class productcatalogproducts_commerce_tax_category_enum_param(str, Enum):
    """productcatalogproducts_commerce_tax_category_enum_param enum values."""

    FB_ANIMAL = "FB_ANIMAL"
    FB_ANIMAL_SUPP = "FB_ANIMAL_SUPP"
    FB_APRL = "FB_APRL"
    FB_APRL_ACCESSORIES = "FB_APRL_ACCESSORIES"
    FB_APRL_ATHL_UNIF = "FB_APRL_ATHL_UNIF"
    FB_APRL_CASES = "FB_APRL_CASES"
    FB_APRL_CLOTHING = "FB_APRL_CLOTHING"
    FB_APRL_COSTUME = "FB_APRL_COSTUME"
    FB_APRL_CSTM = "FB_APRL_CSTM"
    FB_APRL_FORMAL = "FB_APRL_FORMAL"
    FB_APRL_HANDBAG = "FB_APRL_HANDBAG"
    FB_APRL_JEWELRY = "FB_APRL_JEWELRY"
    FB_APRL_SHOE = "FB_APRL_SHOE"
    FB_APRL_SHOE_ACC = "FB_APRL_SHOE_ACC"
    FB_APRL_SWIM = "FB_APRL_SWIM"
    FB_APRL_SWIM_CHIL = "FB_APRL_SWIM_CHIL"
    FB_APRL_SWIM_CVR = "FB_APRL_SWIM_CVR"
    FB_ARTS = "FB_ARTS"
    FB_ARTS_HOBBY = "FB_ARTS_HOBBY"
    FB_ARTS_PARTY = "FB_ARTS_PARTY"
    FB_ARTS_PARTY_GIFT_CARD = "FB_ARTS_PARTY_GIFT_CARD"
    FB_ARTS_TICKET = "FB_ARTS_TICKET"
    FB_BABY = "FB_BABY"
    FB_BABY_BATH = "FB_BABY_BATH"
    FB_BABY_BLANKET = "FB_BABY_BLANKET"
    FB_BABY_DIAPER = "FB_BABY_DIAPER"
    FB_BABY_GIFT_SET = "FB_BABY_GIFT_SET"
    FB_BABY_HEALTH = "FB_BABY_HEALTH"
    FB_BABY_NURSING = "FB_BABY_NURSING"
    FB_BABY_POTTY_TRN = "FB_BABY_POTTY_TRN"
    FB_BABY_SAFE = "FB_BABY_SAFE"
    FB_BABY_TOYS = "FB_BABY_TOYS"
    FB_BABY_TRANSPORT = "FB_BABY_TRANSPORT"
    FB_BABY_TRANSPORT_ACC = "FB_BABY_TRANSPORT_ACC"
    FB_BAGS = "FB_BAGS"
    FB_BAGS_BKPK = "FB_BAGS_BKPK"
    FB_BAGS_BOXES = "FB_BAGS_BOXES"
    FB_BAGS_BRFCS = "FB_BAGS_BRFCS"
    FB_BAGS_CSMT_BAG = "FB_BAGS_CSMT_BAG"
    FB_BAGS_DFFL = "FB_BAGS_DFFL"
    FB_BAGS_DIPR = "FB_BAGS_DIPR"
    FB_BAGS_FNNY = "FB_BAGS_FNNY"
    FB_BAGS_GRMT = "FB_BAGS_GRMT"
    FB_BAGS_LUGG = "FB_BAGS_LUGG"
    FB_BAGS_LUG_ACC = "FB_BAGS_LUG_ACC"
    FB_BAGS_MSGR = "FB_BAGS_MSGR"
    FB_BAGS_TOTE = "FB_BAGS_TOTE"
    FB_BAGS_TRN_CAS = "FB_BAGS_TRN_CAS"
    FB_BLDG = "FB_BLDG"
    FB_BLDG_ACC = "FB_BLDG_ACC"
    FB_BLDG_CNSMB = "FB_BLDG_CNSMB"
    FB_BLDG_FENCE = "FB_BLDG_FENCE"
    FB_BLDG_FUEL_TNK = "FB_BLDG_FUEL_TNK"
    FB_BLDG_HT_VNT = "FB_BLDG_HT_VNT"
    FB_BLDG_LOCK = "FB_BLDG_LOCK"
    FB_BLDG_MATRL = "FB_BLDG_MATRL"
    FB_BLDG_PLMB = "FB_BLDG_PLMB"
    FB_BLDG_PUMP = "FB_BLDG_PUMP"
    FB_BLDG_PWRS = "FB_BLDG_PWRS"
    FB_BLDG_STR_TANK = "FB_BLDG_STR_TANK"
    FB_BLDG_S_ENG = "FB_BLDG_S_ENG"
    FB_BLDG_TL_ACC = "FB_BLDG_TL_ACC"
    FB_BLDG_TOOL = "FB_BLDG_TOOL"
    FB_BUSIND = "FB_BUSIND"
    FB_BUSIND_ADVERTISING = "FB_BUSIND_ADVERTISING"
    FB_BUSIND_AGRICULTURE = "FB_BUSIND_AGRICULTURE"
    FB_BUSIND_AUTOMATION = "FB_BUSIND_AUTOMATION"
    FB_BUSIND_HEAVY_MACH = "FB_BUSIND_HEAVY_MACH"
    FB_BUSIND_LAB = "FB_BUSIND_LAB"
    FB_BUSIND_MEDICAL = "FB_BUSIND_MEDICAL"
    FB_BUSIND_RETAIL = "FB_BUSIND_RETAIL"
    FB_BUSIND_SANITARY_CT = "FB_BUSIND_SANITARY_CT"
    FB_BUSIND_SIGN = "FB_BUSIND_SIGN"
    FB_BUSIND_STORAGE = "FB_BUSIND_STORAGE"
    FB_BUSIND_STORAGE_ACC = "FB_BUSIND_STORAGE_ACC"
    FB_BUSIND_WORK_GEAR = "FB_BUSIND_WORK_GEAR"
    FB_CAMERA_ACC = "FB_CAMERA_ACC"
    FB_CAMERA_CAMERA = "FB_CAMERA_CAMERA"
    FB_CAMERA_OPTIC = "FB_CAMERA_OPTIC"
    FB_CAMERA_OPTICS = "FB_CAMERA_OPTICS"
    FB_CAMERA_PHOTO = "FB_CAMERA_PHOTO"
    FB_ELEC = "FB_ELEC"
    FB_ELEC_ACC = "FB_ELEC_ACC"
    FB_ELEC_ARCDADE = "FB_ELEC_ARCDADE"
    FB_ELEC_AUDIO = "FB_ELEC_AUDIO"
    FB_ELEC_CIRCUIT = "FB_ELEC_CIRCUIT"
    FB_ELEC_COMM = "FB_ELEC_COMM"
    FB_ELEC_COMPUTER = "FB_ELEC_COMPUTER"
    FB_ELEC_GPS_ACC = "FB_ELEC_GPS_ACC"
    FB_ELEC_GPS_NAV = "FB_ELEC_GPS_NAV"
    FB_ELEC_GPS_TRK = "FB_ELEC_GPS_TRK"
    FB_ELEC_MARINE = "FB_ELEC_MARINE"
    FB_ELEC_NETWORK = "FB_ELEC_NETWORK"
    FB_ELEC_PART = "FB_ELEC_PART"
    FB_ELEC_PRINT = "FB_ELEC_PRINT"
    FB_ELEC_RADAR = "FB_ELEC_RADAR"
    FB_ELEC_SFTWR = "FB_ELEC_SFTWR"
    FB_ELEC_SPEED_RDR = "FB_ELEC_SPEED_RDR"
    FB_ELEC_TELEVISION = "FB_ELEC_TELEVISION"
    FB_ELEC_TOLL = "FB_ELEC_TOLL"
    FB_ELEC_VIDEO = "FB_ELEC_VIDEO"
    FB_ELEC_VID_GM_ACC = "FB_ELEC_VID_GM_ACC"
    FB_ELEC_VID_GM_CNSL = "FB_ELEC_VID_GM_CNSL"
    FB_FOOD = "FB_FOOD"
    FB_FURN = "FB_FURN"
    FB_FURN_BABY = "FB_FURN_BABY"
    FB_FURN_BENCH = "FB_FURN_BENCH"
    FB_FURN_CART = "FB_FURN_CART"
    FB_FURN_CHAIR = "FB_FURN_CHAIR"
    FB_FURN_CHAIR_ACC = "FB_FURN_CHAIR_ACC"
    FB_FURN_DIVIDE = "FB_FURN_DIVIDE"
    FB_FURN_DIVIDE_ACC = "FB_FURN_DIVIDE_ACC"
    FB_FURN_ENT_CTR = "FB_FURN_ENT_CTR"
    FB_FURN_FUTN = "FB_FURN_FUTN"
    FB_FURN_FUTN_PAD = "FB_FURN_FUTN_PAD"
    FB_FURN_OFFICE = "FB_FURN_OFFICE"
    FB_FURN_OFFICE_ACC = "FB_FURN_OFFICE_ACC"
    FB_FURN_OTTO = "FB_FURN_OTTO"
    FB_FURN_OUTDOOR = "FB_FURN_OUTDOOR"
    FB_FURN_OUTDOOR_ACC = "FB_FURN_OUTDOOR_ACC"
    FB_FURN_SETS = "FB_FURN_SETS"
    FB_FURN_SHELVE_ACC = "FB_FURN_SHELVE_ACC"
    FB_FURN_SHLF = "FB_FURN_SHLF"
    FB_FURN_SOFA = "FB_FURN_SOFA"
    FB_FURN_SOFA_ACC = "FB_FURN_SOFA_ACC"
    FB_FURN_STORAGE = "FB_FURN_STORAGE"
    FB_FURN_TABL = "FB_FURN_TABL"
    FB_FURN_TABL_ACC = "FB_FURN_TABL_ACC"
    FB_GENERIC_TAXABLE = "FB_GENERIC_TAXABLE"
    FB_HLTH = "FB_HLTH"
    FB_HLTH_HLTH = "FB_HLTH_HLTH"
    FB_HLTH_JWL_CR = "FB_HLTH_JWL_CR"
    FB_HLTH_LILP_BLM = "FB_HLTH_LILP_BLM"
    FB_HLTH_LTN_SPF = "FB_HLTH_LTN_SPF"
    FB_HLTH_PRSL_CR = "FB_HLTH_PRSL_CR"
    FB_HLTH_SKN_CR = "FB_HLTH_SKN_CR"
    FB_HMGN = "FB_HMGN"
    FB_HMGN_BATH = "FB_HMGN_BATH"
    FB_HMGN_DCOR = "FB_HMGN_DCOR"
    FB_HMGN_EMGY = "FB_HMGN_EMGY"
    FB_HMGN_FPLC = "FB_HMGN_FPLC"
    FB_HMGN_FPLC_ACC = "FB_HMGN_FPLC_ACC"
    FB_HMGN_GS_SFT = "FB_HMGN_GS_SFT"
    FB_HMGN_HS_ACC = "FB_HMGN_HS_ACC"
    FB_HMGN_HS_APP = "FB_HMGN_HS_APP"
    FB_HMGN_HS_SPL = "FB_HMGN_HS_SPL"
    FB_HMGN_KTCN = "FB_HMGN_KTCN"
    FB_HMGN_LAWN = "FB_HMGN_LAWN"
    FB_HMGN_LGHT = "FB_HMGN_LGHT"
    FB_HMGN_LINN = "FB_HMGN_LINN"
    FB_HMGN_LT_ACC = "FB_HMGN_LT_ACC"
    FB_HMGN_OTDR = "FB_HMGN_OTDR"
    FB_HMGN_POOL = "FB_HMGN_POOL"
    FB_HMGN_SCTY = "FB_HMGN_SCTY"
    FB_HMGN_SMK_ACC = "FB_HMGN_SMK_ACC"
    FB_HMGN_UMBR = "FB_HMGN_UMBR"
    FB_HMGN_UMBR_ACC = "FB_HMGN_UMBR_ACC"
    FB_MDIA = "FB_MDIA"
    FB_MDIA_BOOK = "FB_MDIA_BOOK"
    FB_MDIA_DVDS = "FB_MDIA_DVDS"
    FB_MDIA_MAG = "FB_MDIA_MAG"
    FB_MDIA_MANL = "FB_MDIA_MANL"
    FB_MDIA_MUSC = "FB_MDIA_MUSC"
    FB_MDIA_PRJ_PLN = "FB_MDIA_PRJ_PLN"
    FB_MDIA_SHT_MUS = "FB_MDIA_SHT_MUS"
    FB_OFFC = "FB_OFFC"
    FB_OFFC_BKAC = "FB_OFFC_BKAC"
    FB_OFFC_CRTS = "FB_OFFC_CRTS"
    FB_OFFC_DSKP = "FB_OFFC_DSKP"
    FB_OFFC_EQIP = "FB_OFFC_EQIP"
    FB_OFFC_FLNG = "FB_OFFC_FLNG"
    FB_OFFC_GNRL = "FB_OFFC_GNRL"
    FB_OFFC_INSTM = "FB_OFFC_INSTM"
    FB_OFFC_LP_DSK = "FB_OFFC_LP_DSK"
    FB_OFFC_MATS = "FB_OFFC_MATS"
    FB_OFFC_NM_PLT = "FB_OFFC_NM_PLT"
    FB_OFFC_PPR_HNDL = "FB_OFFC_PPR_HNDL"
    FB_OFFC_PRSNT_SPL = "FB_OFFC_PRSNT_SPL"
    FB_OFFC_SEALR = "FB_OFFC_SEALR"
    FB_OFFC_SHIP_SPL = "FB_OFFC_SHIP_SPL"
    FB_RLGN = "FB_RLGN"
    FB_RLGN_CMNY = "FB_RLGN_CMNY"
    FB_RLGN_ITEM = "FB_RLGN_ITEM"
    FB_RLGN_WEDD = "FB_RLGN_WEDD"
    FB_SFTWR = "FB_SFTWR"
    FB_SFWR_CMPTR = "FB_SFWR_CMPTR"
    FB_SFWR_DGTL_GD = "FB_SFWR_DGTL_GD"
    FB_SFWR_GAME = "FB_SFWR_GAME"
    FB_SHIPPING = "FB_SHIPPING"
    FB_SPOR = "FB_SPOR"
    FB_SPORT_ATHL = "FB_SPORT_ATHL"
    FB_SPORT_ATHL_CLTH = "FB_SPORT_ATHL_CLTH"
    FB_SPORT_ATHL_SHOE = "FB_SPORT_ATHL_SHOE"
    FB_SPORT_ATHL_SPRT = "FB_SPORT_ATHL_SPRT"
    FB_SPORT_EXRCS = "FB_SPORT_EXRCS"
    FB_SPORT_INDR_GM = "FB_SPORT_INDR_GM"
    FB_SPORT_OTDR_GM = "FB_SPORT_OTDR_GM"
    FB_TOYS = "FB_TOYS"
    FB_TOYS_EQIP = "FB_TOYS_EQIP"
    FB_TOYS_GAME = "FB_TOYS_GAME"
    FB_TOYS_PZZL = "FB_TOYS_PZZL"
    FB_TOYS_TMRS = "FB_TOYS_TMRS"
    FB_TOYS_TOYS = "FB_TOYS_TOYS"
    FB_VEHI = "FB_VEHI"
    FB_VEHI_PART = "FB_VEHI_PART"


class productcatalogproducts_wa_compliance_category_enum_param(str, Enum):
    """productcatalogproducts_wa_compliance_category_enum_param enum values."""

    COUNTRY_ORIGIN_EXEMPT = "COUNTRY_ORIGIN_EXEMPT"
    DEFAULT = "DEFAULT"


class productcatalogvehicles_state_of_vehicle_enum_param(str, Enum):
    """productcatalogvehicles_state_of_vehicle_enum_param enum values."""

    CPO = "CPO"
    NEW = "NEW"
    USED = "USED"


class productcatalogproducts_error_priority_enum_param(str, Enum):
    """productcatalogproducts_error_priority_enum_param enum values."""

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class productcatalogproducts_condition_enum_param(str, Enum):
    """productcatalogproducts_condition_enum_param enum values."""

    cpo = "cpo"
    new = "new"
    open_box_new = "open_box_new"
    refurbished = "refurbished"
    used = "used"
    used_fair = "used_fair"
    used_good = "used_good"
    used_like_new = "used_like_new"


class productcatalogagencies_permitted_roles_enum_param(str, Enum):
    """productcatalogagencies_permitted_roles_enum_param enum values."""

    ADMIN = "ADMIN"
    ADVERTISER = "ADVERTISER"


class productcatalogvehicles_availability_enum_param(str, Enum):
    """productcatalogvehicles_availability_enum_param enum values."""

    AVAILABLE = "AVAILABLE"
    NOT_AVAILABLE = "NOT_AVAILABLE"
    PENDING = "PENDING"
    UNKNOWN = "UNKNOWN"


class productcataloghotel_rooms_batch_standard_enum_param(str, Enum):
    """productcataloghotel_rooms_batch_standard_enum_param enum values."""

    google = "google"


class productcatalogitems_batch_item_sub_type_enum_param(str, Enum):
    """productcatalogitems_batch_item_sub_type_enum_param enum values."""

    APPLIANCES = "APPLIANCES"
    BABY_FEEDING = "BABY_FEEDING"
    BABY_TRANSPORT = "BABY_TRANSPORT"
    BEAUTY = "BEAUTY"
    BEDDING = "BEDDING"
    CAMERAS = "CAMERAS"
    CELL_PHONES_AND_SMART_WATCHES = "CELL_PHONES_AND_SMART_WATCHES"
    CLEANING_SUPPLIES = "CLEANING_SUPPLIES"
    CLOTHING = "CLOTHING"
    CLOTHING_ACCESSORIES = "CLOTHING_ACCESSORIES"
    COMPUTERS_AND_TABLETS = "COMPUTERS_AND_TABLETS"
    DIAPERING_AND_POTTY_TRAINING = "DIAPERING_AND_POTTY_TRAINING"
    ELECTRONICS_ACCESSORIES = "ELECTRONICS_ACCESSORIES"
    FURNITURE = "FURNITURE"
    HEALTH = "HEALTH"
    HOME_GOODS = "HOME_GOODS"
    JEWELRY = "JEWELRY"
    NURSERY = "NURSERY"
    PRINTERS_AND_SCANNERS = "PRINTERS_AND_SCANNERS"
    PROJECTORS = "PROJECTORS"
    SHOES_AND_FOOTWEAR = "SHOES_AND_FOOTWEAR"
    SOFTWARE = "SOFTWARE"
    TOYS = "TOYS"
    TVS_AND_MONITORS = "TVS_AND_MONITORS"
    VIDEO_GAME_CONSOLES_AND_VIDEO_GAMES = "VIDEO_GAME_CONSOLES_AND_VIDEO_GAMES"
    WATCHES = "WATCHES"


class productcatalogproducts_marked_for_product_launch_enum_param(str, Enum):
    """productcatalogproducts_marked_for_product_launch_enum_param enum values."""

    default = "default"
    marked = "marked"
    not_marked = "not_marked"


class productcatalogvehicles_condition_enum_param(str, Enum):
    """productcatalogvehicles_condition_enum_param enum values."""

    EXCELLENT = "EXCELLENT"
    FAIR = "FAIR"
    GOOD = "GOOD"
    NONE = "NONE"
    OTHER = "OTHER"
    POOR = "POOR"
    VERY_GOOD = "VERY_GOOD"


class productcatalogcategories_categorization_criteria_enum_param(str, Enum):
    """productcatalogcategories_categorization_criteria_enum_param enum values."""

    BRAND = "BRAND"
    CATEGORY = "CATEGORY"
    PRODUCT_TYPE = "PRODUCT_TYPE"


class productcatalogproduct_feeds_override_type_enum_param(str, Enum):
    """productcatalogproduct_feeds_override_type_enum_param enum values."""

    BATCH_API_LANGUAGE_OR_COUNTRY = "BATCH_API_LANGUAGE_OR_COUNTRY"
    CATALOG_SEGMENT_CUSTOMIZE_DEFAULT = "CATALOG_SEGMENT_CUSTOMIZE_DEFAULT"
    COUNTRY = "COUNTRY"
    LANGUAGE = "LANGUAGE"
    LANGUAGE_AND_COUNTRY = "LANGUAGE_AND_COUNTRY"
    LOCAL = "LOCAL"
    SMART_PIXEL_LANGUAGE_OR_COUNTRY = "SMART_PIXEL_LANGUAGE_OR_COUNTRY"
    VERSION = "VERSION"


class productcatalogproduct_feeds_encoding_enum_param(str, Enum):
    """productcatalogproduct_feeds_encoding_enum_param enum values."""

    AUTODETECT = "AUTODETECT"
    LATIN1 = "LATIN1"
    UTF16BE = "UTF16BE"
    UTF16LE = "UTF16LE"
    UTF32BE = "UTF32BE"
    UTF32LE = "UTF32LE"
    UTF8 = "UTF8"


class productcatalogdiagnostics_affected_entities_enum_param(str, Enum):
    """productcatalogdiagnostics_affected_entities_enum_param enum values."""

    product_catalog = "product_catalog"
    product_event = "product_event"
    product_item = "product_item"
    product_set = "product_set"


class productcatalogcreator_asset_creatives_moderation_status_enum_param(str, Enum):
    """productcatalogcreator_asset_creatives_moderation_status_enum_param enum values."""

    ARCHIVED = "ARCHIVED"
    ELIGIBLE = "ELIGIBLE"
    EXPIRED = "EXPIRED"
    INELIGIBLE = "INELIGIBLE"
    IN_REVIEW = "IN_REVIEW"
    PAUSED = "PAUSED"
    UNKNOWN = "UNKNOWN"


class productcatalogproducts_gender_enum_param(str, Enum):
    """productcatalogproducts_gender_enum_param enum values."""

    female = "female"
    male = "male"
    unisex = "unisex"


class productcatalogproduct_feeds_item_sub_type_enum_param(str, Enum):
    """productcatalogproduct_feeds_item_sub_type_enum_param enum values."""

    APPLIANCES = "APPLIANCES"
    BABY_FEEDING = "BABY_FEEDING"
    BABY_TRANSPORT = "BABY_TRANSPORT"
    BEAUTY = "BEAUTY"
    BEDDING = "BEDDING"
    CAMERAS = "CAMERAS"
    CELL_PHONES_AND_SMART_WATCHES = "CELL_PHONES_AND_SMART_WATCHES"
    CLEANING_SUPPLIES = "CLEANING_SUPPLIES"
    CLOTHING = "CLOTHING"
    CLOTHING_ACCESSORIES = "CLOTHING_ACCESSORIES"
    COMPUTERS_AND_TABLETS = "COMPUTERS_AND_TABLETS"
    DIAPERING_AND_POTTY_TRAINING = "DIAPERING_AND_POTTY_TRAINING"
    ELECTRONICS_ACCESSORIES = "ELECTRONICS_ACCESSORIES"
    FURNITURE = "FURNITURE"
    HEALTH = "HEALTH"
    HOME_GOODS = "HOME_GOODS"
    JEWELRY = "JEWELRY"
    NURSERY = "NURSERY"
    PRINTERS_AND_SCANNERS = "PRINTERS_AND_SCANNERS"
    PROJECTORS = "PROJECTORS"
    SHOES_AND_FOOTWEAR = "SHOES_AND_FOOTWEAR"
    SOFTWARE = "SOFTWARE"
    TOYS = "TOYS"
    TVS_AND_MONITORS = "TVS_AND_MONITORS"
    VIDEO_GAME_CONSOLES_AND_VIDEO_GAMES = "VIDEO_GAME_CONSOLES_AND_VIDEO_GAMES"
    WATCHES = "WATCHES"


class productcatalogproducts_origin_country_enum_param(str, Enum):
    """productcatalogproducts_origin_country_enum_param enum values."""

    AD = "AD"
    AE = "AE"
    AF = "AF"
    AG = "AG"
    AI = "AI"
    AL = "AL"
    AM = "AM"
    AN = "AN"
    AO = "AO"
    AQ = "AQ"
    AR = "AR"
    AS = "AS"
    AT = "AT"
    AU = "AU"
    AW = "AW"
    AX = "AX"
    AZ = "AZ"
    BA = "BA"
    BB = "BB"
    BD = "BD"
    BE = "BE"
    BF = "BF"
    BG = "BG"
    BH = "BH"
    BI = "BI"
    BJ = "BJ"
    BL = "BL"
    BM = "BM"
    BN = "BN"
    BO = "BO"
    BQ = "BQ"
    BR = "BR"
    BS = "BS"
    BT = "BT"
    BV = "BV"
    BW = "BW"
    BY = "BY"
    BZ = "BZ"
    CA = "CA"
    CC = "CC"
    CD = "CD"
    CF = "CF"
    CG = "CG"
    CH = "CH"
    CI = "CI"
    CK = "CK"
    CL = "CL"
    CM = "CM"
    CN = "CN"
    CO = "CO"
    CR = "CR"
    CU = "CU"
    CV = "CV"
    CW = "CW"
    CX = "CX"
    CY = "CY"
    CZ = "CZ"
    DE = "DE"
    DJ = "DJ"
    DK = "DK"
    DM = "DM"
    DO = "DO"
    DZ = "DZ"
    EC = "EC"
    EE = "EE"
    EG = "EG"
    EH = "EH"
    ER = "ER"
    ES = "ES"
    ET = "ET"
    FI = "FI"
    FJ = "FJ"
    FK = "FK"
    FM = "FM"
    FO = "FO"
    FR = "FR"
    GA = "GA"
    GB = "GB"
    GD = "GD"
    GE = "GE"
    GF = "GF"
    GG = "GG"
    GH = "GH"
    GI = "GI"
    GL = "GL"
    GM = "GM"
    GN = "GN"
    GP = "GP"
    GQ = "GQ"
    GR = "GR"
    GS = "GS"
    GT = "GT"
    GU = "GU"
    GW = "GW"
    GY = "GY"
    HK = "HK"
    HM = "HM"
    HN = "HN"
    HR = "HR"
    HT = "HT"
    HU = "HU"
    ID = "ID"
    IE = "IE"
    IL = "IL"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IQ = "IQ"
    IR = "IR"
    IS = "IS"
    IT = "IT"
    JE = "JE"
    JM = "JM"
    JO = "JO"
    JP = "JP"
    KE = "KE"
    KG = "KG"
    KH = "KH"
    KI = "KI"
    KM = "KM"
    KN = "KN"
    KP = "KP"
    KR = "KR"
    KW = "KW"
    KY = "KY"
    KZ = "KZ"
    LA = "LA"
    LB = "LB"
    LC = "LC"
    LI = "LI"
    LK = "LK"
    LR = "LR"
    LS = "LS"
    LT = "LT"
    LU = "LU"
    LV = "LV"
    LY = "LY"
    MA = "MA"
    MC = "MC"
    MD = "MD"
    ME = "ME"
    MF = "MF"
    MG = "MG"
    MH = "MH"
    MK = "MK"
    ML = "ML"
    MM = "MM"
    MN = "MN"
    MO = "MO"
    MP = "MP"
    MQ = "MQ"
    MR = "MR"
    MS = "MS"
    MT = "MT"
    MU = "MU"
    MV = "MV"
    MW = "MW"
    MX = "MX"
    MY = "MY"
    MZ = "MZ"
    NA = "NA"
    NC = "NC"
    NE = "NE"
    NF = "NF"
    NG = "NG"
    NI = "NI"
    NL = "NL"
    NO = "NO"
    NP = "NP"
    NR = "NR"
    NU = "NU"
    NZ = "NZ"
    OM = "OM"
    PA = "PA"
    PE = "PE"
    PF = "PF"
    PG = "PG"
    PH = "PH"
    PK = "PK"
    PL = "PL"
    PM = "PM"
    PN = "PN"
    PR = "PR"
    PS = "PS"
    PT = "PT"
    PW = "PW"
    PY = "PY"
    QA = "QA"
    RE = "RE"
    RO = "RO"
    RS = "RS"
    RU = "RU"
    RW = "RW"
    SA = "SA"
    SB = "SB"
    SC = "SC"
    SD = "SD"
    SE = "SE"
    SG = "SG"
    SH = "SH"
    SI = "SI"
    SJ = "SJ"
    SK = "SK"
    SL = "SL"
    SM = "SM"
    SN = "SN"
    SO = "SO"
    SR = "SR"
    SS = "SS"
    ST = "ST"
    SV = "SV"
    SX = "SX"
    SY = "SY"
    SZ = "SZ"
    TC = "TC"
    TD = "TD"
    TF = "TF"
    TG = "TG"
    TH = "TH"
    TJ = "TJ"
    TK = "TK"
    TL = "TL"
    TM = "TM"
    TN = "TN"
    TO = "TO"
    TR = "TR"
    TT = "TT"
    TV = "TV"
    TW = "TW"
    TZ = "TZ"
    UA = "UA"
    UG = "UG"
    UM = "UM"
    US = "US"
    UY = "UY"
    UZ = "UZ"
    VA = "VA"
    VC = "VC"
    VE = "VE"
    VG = "VG"
    VI = "VI"
    VN = "VN"
    VU = "VU"
    WF = "WF"
    WS = "WS"
    XK = "XK"
    YE = "YE"
    YT = "YT"
    ZA = "ZA"
    ZM = "ZM"
    ZW = "ZW"


class productcatalogassigned_users_tasks_enum_param(str, Enum):
    """productcatalogassigned_users_tasks_enum_param enum values."""

    AA_ANALYZE = "AA_ANALYZE"
    ADVERTISE = "ADVERTISE"
    MANAGE = "MANAGE"
    MANAGE_AR = "MANAGE_AR"


class productcatalogproducts_availability_enum_param(str, Enum):
    """productcatalogproducts_availability_enum_param enum values."""

    AVAILABLE_FOR_ORDER = "available for order"
    discontinued = "discontinued"
    IN_STOCK = "in stock"
    mark_as_sold = "mark_as_sold"
    OUT_OF_STOCK = "out of stock"
    pending = "pending"
    preorder = "preorder"


class productcatalogvehicles_transmission_enum_param(str, Enum):
    """productcatalogvehicles_transmission_enum_param enum values."""

    AUTOMATIC = "AUTOMATIC"
    MANUAL = "MANUAL"
    NONE = "NONE"
    OTHER = "OTHER"


class productcatalogevent_stats_breakdowns_enum_param(str, Enum):
    """productcatalogevent_stats_breakdowns_enum_param enum values."""

    DEVICE_TYPE = "DEVICE_TYPE"


class productcatalogdiagnostics_severities_enum_param(str, Enum):
    """productcatalogdiagnostics_severities_enum_param enum values."""

    MUST_FIX = "MUST_FIX"
    OPPORTUNITY = "OPPORTUNITY"


class productcatalogvehicles_body_style_enum_param(str, Enum):
    """productcatalogvehicles_body_style_enum_param enum values."""

    CONVERTIBLE = "CONVERTIBLE"
    COUPE = "COUPE"
    CROSSOVER = "CROSSOVER"
    ESTATE = "ESTATE"
    GRANDTOURER = "GRANDTOURER"
    HATCHBACK = "HATCHBACK"
    MINIBUS = "MINIBUS"
    MINIVAN = "MINIVAN"
    MPV = "MPV"
    NONE = "NONE"
    OTHER = "OTHER"
    PICKUP = "PICKUP"
    ROADSTER = "ROADSTER"
    SALOON = "SALOON"
    SEDAN = "SEDAN"
    SMALL_CAR = "SMALL_CAR"
    SPORTSCAR = "SPORTSCAR"
    SUPERCAR = "SUPERCAR"
    SUPERMINI = "SUPERMINI"
    SUV = "SUV"
    TRUCK = "TRUCK"
    VAN = "VAN"
    WAGON = "WAGON"


class productcatalogvehicles_drivetrain_enum_param(str, Enum):
    """productcatalogvehicles_drivetrain_enum_param enum values."""

    AWD = "AWD"
    FOUR_WD = "FOUR_WD"
    FWD = "FWD"
    NONE = "NONE"
    OTHER = "OTHER"
    RWD = "RWD"
    TWO_WD = "TWO_WD"


class productcatalogdiagnostics_affected_features_enum_param(str, Enum):
    """productcatalogdiagnostics_affected_features_enum_param enum values."""

    augmented_reality = "augmented_reality"
    checkout = "checkout"


class productcatalogvehicles_fuel_type_enum_param(str, Enum):
    """productcatalogvehicles_fuel_type_enum_param enum values."""

    DIESEL = "DIESEL"
    ELECTRIC = "ELECTRIC"
    FLEX = "FLEX"
    GASOLINE = "GASOLINE"
    HYBRID = "HYBRID"
    NONE = "NONE"
    OTHER = "OTHER"
    PETROL = "PETROL"
    PLUGIN_HYBRID = "PLUGIN_HYBRID"


class productcatalogcheck_batch_request_status_error_priority_enum_param(str, Enum):
    """productcatalogcheck_batch_request_status_error_priority_enum_param enum values."""

    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"


class productcatalogproduct_feeds_delimiter_enum_param(str, Enum):
    """productcatalogproduct_feeds_delimiter_enum_param enum values."""

    AUTODETECT = "AUTODETECT"
    BAR = "BAR"
    COMMA = "COMMA"
    SEMICOLON = "SEMICOLON"
    TAB = "TAB"
    TILDE = "TILDE"


class productcatalogmarketplace_partner_signals_event_name_enum_param(str, Enum):
    """productcatalogmarketplace_partner_signals_event_name_enum_param enum values."""

    ADD_TO_CART = "ADD_TO_CART"
    PURCHASE = "PURCHASE"
    TEST = "TEST"
    VIEW_ITEM = "VIEW_ITEM"


class productcatalogproducts_visibility_enum_param(str, Enum):
    """productcatalogproducts_visibility_enum_param enum values."""

    published = "published"
    staging = "staging"


class productcatalogdiagnostics_types_enum_param(str, Enum):
    """productcatalogdiagnostics_types_enum_param enum values."""

    AR_VISIBILITY_ISSUES = "AR_VISIBILITY_ISSUES"
    ATTRIBUTES_INVALID = "ATTRIBUTES_INVALID"
    ATTRIBUTES_MISSING = "ATTRIBUTES_MISSING"
    CATEGORY = "CATEGORY"
    CHECKOUT = "CHECKOUT"
    DA_VISIBILITY_ISSUES = "DA_VISIBILITY_ISSUES"
    EVENT_SOURCE_ISSUES = "EVENT_SOURCE_ISSUES"
    IMAGE_QUALITY = "IMAGE_QUALITY"
    LOW_QUALITY_TITLE_AND_DESCRIPTION = "LOW_QUALITY_TITLE_AND_DESCRIPTION"
    POLICY_VIOLATION = "POLICY_VIOLATION"
    SHOPS_VISIBILITY_ISSUES = "SHOPS_VISIBILITY_ISSUES"


class productcatalogproduct_feeds_ingestion_source_type_enum_param(str, Enum):
    """productcatalogproduct_feeds_ingestion_source_type_enum_param enum values."""

    PRIMARY_FEED = "PRIMARY_FEED"
    SUPPLEMENTARY_FEED = "SUPPLEMENTARY_FEED"


class productcatalogproduct_feeds_quoted_fields_mode_enum_param(str, Enum):
    """productcatalogproduct_feeds_quoted_fields_mode_enum_param enum values."""

    autodetect = "autodetect"
    off = "off"
    on = "on"


class productcatalogproducts_age_group_enum_param(str, Enum):
    """productcatalogproducts_age_group_enum_param enum values."""

    adult = "adult"
    ALL_AGES = "all ages"
    infant = "infant"
    kids = "kids"
    newborn = "newborn"
    teen = "teen"
    toddler = "toddler"


class productcatalogvehicles_vehicle_type_enum_param(str, Enum):
    """productcatalogvehicles_vehicle_type_enum_param enum values."""

    BOAT = "BOAT"
    CAR_TRUCK = "CAR_TRUCK"
    COMMERCIAL = "COMMERCIAL"
    MOTORCYCLE = "MOTORCYCLE"
    OTHER = "OTHER"
    POWERSPORT = "POWERSPORT"
    RV_CAMPER = "RV_CAMPER"
    TRAILER = "TRAILER"


class productcatalogdiagnostics_affected_channels_enum_param(str, Enum):
    """productcatalogdiagnostics_affected_channels_enum_param enum values."""

    b2c_marketplace = "b2c_marketplace"
    c2c_marketplace = "c2c_marketplace"
    da = "da"
    daily_deals = "daily_deals"
    daily_deals_legacy = "daily_deals_legacy"
    ig_product_tagging = "ig_product_tagging"
    marketplace = "marketplace"
    marketplace_ads_deprecated = "marketplace_ads_deprecated"
    marketplace_shops = "marketplace_shops"
    mini_shops = "mini_shops"
    offline_conversions = "offline_conversions"
    shops = "shops"
    universal_checkout = "universal_checkout"
    whatsapp = "whatsapp"


class productcatalogproducts_error_type_enum_param(str, Enum):
    """productcatalogproducts_error_type_enum_param enum values."""

    ADDRESS_BLOCKLISTED_IN_MARKET = "ADDRESS_BLOCKLISTED_IN_MARKET"
    AGGREGATED_LOCALIZATION_ISSUES = "AGGREGATED_LOCALIZATION_ISSUES"
    APP_HAS_NO_AEM_SETUP = "APP_HAS_NO_AEM_SETUP"
    AR_DELETED_DUE_TO_UPDATE = "AR_DELETED_DUE_TO_UPDATE"
    AR_POLICY_VIOLATED = "AR_POLICY_VIOLATED"
    AVAILABLE = "AVAILABLE"
    BAD_QUALITY_IMAGE = "BAD_QUALITY_IMAGE"
    BIG_CATALOG_WITH_ALL_ITEMS_IN_STOCK = "BIG_CATALOG_WITH_ALL_ITEMS_IN_STOCK"
    BIZ_MSG_AI_AGENT_DISABLED_BY_USER = "BIZ_MSG_AI_AGENT_DISABLED_BY_USER"
    BIZ_MSG_GEN_AI_POLICY_VIOLATED = "BIZ_MSG_GEN_AI_POLICY_VIOLATED"
    CANNOT_EDIT_SUBSCRIPTION_PRODUCTS = "CANNOT_EDIT_SUBSCRIPTION_PRODUCTS"
    CATALOG_NOT_CONNECTED_TO_EVENT_SOURCE = "CATALOG_NOT_CONNECTED_TO_EVENT_SOURCE"
    CHECKOUT_DISABLED_BY_USER = "CHECKOUT_DISABLED_BY_USER"
    COMMERCE_ACCOUNT_LEGAL_ADDRESS_INVALID = "COMMERCE_ACCOUNT_LEGAL_ADDRESS_INVALID"
    COMMERCE_ACCOUNT_NOT_LEGALLY_COMPLIANT = "COMMERCE_ACCOUNT_NOT_LEGALLY_COMPLIANT"
    CRAWLED_AVAILABILITY_MISMATCH = "CRAWLED_AVAILABILITY_MISMATCH"
    DA_DISABLED_BY_USER = "DA_DISABLED_BY_USER"
    DA_POLICY_UNFIT_FOR_AUDIENCE = "DA_POLICY_UNFIT_FOR_AUDIENCE"
    DA_POLICY_VIOLATION = "DA_POLICY_VIOLATION"
    DELETED_ITEM = "DELETED_ITEM"
    DIGITAL_GOODS_NOT_AVAILABLE_FOR_CHECKOUT = "DIGITAL_GOODS_NOT_AVAILABLE_FOR_CHECKOUT"
    DUPLICATE_IMAGES = "DUPLICATE_IMAGES"
    DUPLICATE_TITLE_AND_DESCRIPTION = "DUPLICATE_TITLE_AND_DESCRIPTION"
    EMPTY_AVAILABILITY = "EMPTY_AVAILABILITY"
    EMPTY_CONDITION = "EMPTY_CONDITION"
    EMPTY_DESCRIPTION = "EMPTY_DESCRIPTION"
    EMPTY_IMAGE_URL = "EMPTY_IMAGE_URL"
    EMPTY_PRICE = "EMPTY_PRICE"
    EMPTY_PRODUCT_URL = "EMPTY_PRODUCT_URL"
    EMPTY_SELLER_DESCRIPTION = "EMPTY_SELLER_DESCRIPTION"
    EMPTY_TITLE = "EMPTY_TITLE"
    EXTERNAL_MERCHANT_ID_MISMATCH = "EXTERNAL_MERCHANT_ID_MISMATCH"
    GENERIC_INVALID_FIELD = "GENERIC_INVALID_FIELD"
    GROUPS_DISABLED_BY_USER = "GROUPS_DISABLED_BY_USER"
    HIDDEN_UNTIL_PRODUCT_LAUNCH = "HIDDEN_UNTIL_PRODUCT_LAUNCH"
    ILLEGAL_PRODUCT_CATEGORY = "ILLEGAL_PRODUCT_CATEGORY"
    IMAGE_FETCH_FAILED = "IMAGE_FETCH_FAILED"
    IMAGE_FETCH_FAILED_BAD_GATEWAY = "IMAGE_FETCH_FAILED_BAD_GATEWAY"
    IMAGE_FETCH_FAILED_FILE_SIZE_EXCEEDED = "IMAGE_FETCH_FAILED_FILE_SIZE_EXCEEDED"
    IMAGE_FETCH_FAILED_FORBIDDEN = "IMAGE_FETCH_FAILED_FORBIDDEN"
    IMAGE_FETCH_FAILED_LINK_BROKEN = "IMAGE_FETCH_FAILED_LINK_BROKEN"
    IMAGE_FETCH_FAILED_TIMED_OUT = "IMAGE_FETCH_FAILED_TIMED_OUT"
    IMAGE_RESOLUTION_LOW = "IMAGE_RESOLUTION_LOW"
    INACTIVE_SHOPIFY_PRODUCT = "INACTIVE_SHOPIFY_PRODUCT"
    INVALID_COMMERCE_TAX_CATEGORY = "INVALID_COMMERCE_TAX_CATEGORY"
    INVALID_CONSOLIDATED_LOCALITY_INFORMATION = "INVALID_CONSOLIDATED_LOCALITY_INFORMATION"
    INVALID_CONTENT_ID = "INVALID_CONTENT_ID"
    INVALID_DEALER_COMMUNICATION_PARAMETERS = "INVALID_DEALER_COMMUNICATION_PARAMETERS"
    INVALID_DMA_CODES = "INVALID_DMA_CODES"
    INVALID_FB_PAGE_ID = "INVALID_FB_PAGE_ID"
    INVALID_IMAGES = "INVALID_IMAGES"
    INVALID_MONETIZER_RETURN_POLICY = "INVALID_MONETIZER_RETURN_POLICY"
    INVALID_OFFER_DISCLAIMER_URL = "INVALID_OFFER_DISCLAIMER_URL"
    INVALID_OFFER_END_DATE = "INVALID_OFFER_END_DATE"
    INVALID_PRE_ORDER_PARAMS = "INVALID_PRE_ORDER_PARAMS"
    INVALID_RANGE_FOR_AREA_SIZE = "INVALID_RANGE_FOR_AREA_SIZE"
    INVALID_RANGE_FOR_BUILT_UP_AREA_SIZE = "INVALID_RANGE_FOR_BUILT_UP_AREA_SIZE"
    INVALID_RANGE_FOR_NUM_OF_BATHS = "INVALID_RANGE_FOR_NUM_OF_BATHS"
    INVALID_RANGE_FOR_NUM_OF_BEDS = "INVALID_RANGE_FOR_NUM_OF_BEDS"
    INVALID_RANGE_FOR_NUM_OF_ROOMS = "INVALID_RANGE_FOR_NUM_OF_ROOMS"
    INVALID_RANGE_FOR_PARKING_SPACES = "INVALID_RANGE_FOR_PARKING_SPACES"
    INVALID_SHELTER_PAGE_ID = "INVALID_SHELTER_PAGE_ID"
    INVALID_SHIPPING_PROFILE_PARAMS = "INVALID_SHIPPING_PROFILE_PARAMS"
    INVALID_SUBSCRIPTION_DISABLE_PARAMS = "INVALID_SUBSCRIPTION_DISABLE_PARAMS"
    INVALID_SUBSCRIPTION_ENABLE_PARAMS = "INVALID_SUBSCRIPTION_ENABLE_PARAMS"
    INVALID_SUBSCRIPTION_PARAMS = "INVALID_SUBSCRIPTION_PARAMS"
    INVALID_TAX_EXTENSION_STATE = "INVALID_TAX_EXTENSION_STATE"
    INVALID_VEHICLE_STATE = "INVALID_VEHICLE_STATE"
    INVALID_VIRTUAL_TOUR_URL_DOMAIN = "INVALID_VIRTUAL_TOUR_URL_DOMAIN"
    INVENTORY_ZERO_AVAILABILITY_IN_STOCK = "INVENTORY_ZERO_AVAILABILITY_IN_STOCK"
    IN_ANOTHER_PRODUCT_LAUNCH = "IN_ANOTHER_PRODUCT_LAUNCH"
    ITEM_GROUP_NOT_SPECIFIED = "ITEM_GROUP_NOT_SPECIFIED"
    ITEM_NOT_SHIPPABLE_FOR_SCA_SHOP = "ITEM_NOT_SHIPPABLE_FOR_SCA_SHOP"
    ITEM_OVERRIDE_EMPTY_AVAILABILITY = "ITEM_OVERRIDE_EMPTY_AVAILABILITY"
    ITEM_OVERRIDE_EMPTY_PRICE = "ITEM_OVERRIDE_EMPTY_PRICE"
    ITEM_OVERRIDE_NOT_VISIBLE = "ITEM_OVERRIDE_NOT_VISIBLE"
    ITEM_PRICE_NOT_POSITIVE = "ITEM_PRICE_NOT_POSITIVE"
    ITEM_STALE_OUT_OF_STOCK = "ITEM_STALE_OUT_OF_STOCK"
    MARKETPLACE_DISABLED_BY_USER = "MARKETPLACE_DISABLED_BY_USER"
    MARKETPLACE_PARTNER_AUCTION_NO_BID_CLOSE_TIME = "MARKETPLACE_PARTNER_AUCTION_NO_BID_CLOSE_TIME"
    MARKETPLACE_PARTNER_CURRENCY_NOT_VALID = "MARKETPLACE_PARTNER_CURRENCY_NOT_VALID"
    MARKETPLACE_PARTNER_LISTING_COUNTRY_NOT_MATCH_CATALOG = (
        "MARKETPLACE_PARTNER_LISTING_COUNTRY_NOT_MATCH_CATALOG"
    )
    MARKETPLACE_PARTNER_LISTING_LIMIT_EXCEEDED = "MARKETPLACE_PARTNER_LISTING_LIMIT_EXCEEDED"
    MARKETPLACE_PARTNER_MISSING_LATLONG = "MARKETPLACE_PARTNER_MISSING_LATLONG"
    MARKETPLACE_PARTNER_MISSING_SHIPPING_COST = "MARKETPLACE_PARTNER_MISSING_SHIPPING_COST"
    MARKETPLACE_PARTNER_NOT_LOCAL_ITEM = "MARKETPLACE_PARTNER_NOT_LOCAL_ITEM"
    MARKETPLACE_PARTNER_NOT_SHIPPED_ITEM = "MARKETPLACE_PARTNER_NOT_SHIPPED_ITEM"
    MARKETPLACE_PARTNER_POLICY_VIOLATION = "MARKETPLACE_PARTNER_POLICY_VIOLATION"
    MARKETPLACE_PARTNER_RULE_LISTING_LIMIT_EXCEEDED = (
        "MARKETPLACE_PARTNER_RULE_LISTING_LIMIT_EXCEEDED"
    )
    MARKETPLACE_PARTNER_SELLER_BANNED = "MARKETPLACE_PARTNER_SELLER_BANNED"
    MARKETPLACE_PARTNER_SELLER_NOT_VALID = "MARKETPLACE_PARTNER_SELLER_NOT_VALID"
    MINI_SHOPS_DISABLED_BY_USER = "MINI_SHOPS_DISABLED_BY_USER"
    MISSING_CHECKOUT = "MISSING_CHECKOUT"
    MISSING_CHECKOUT_CURRENCY = "MISSING_CHECKOUT_CURRENCY"
    MISSING_COLOR = "MISSING_COLOR"
    MISSING_COUNTRY_OVERRIDE_IN_SHIPPING_PROFILE = "MISSING_COUNTRY_OVERRIDE_IN_SHIPPING_PROFILE"
    MISSING_EVENT = "MISSING_EVENT"
    MISSING_INDIA_COMPLIANCE_FIELDS = "MISSING_INDIA_COMPLIANCE_FIELDS"
    MISSING_SHIPPING_PROFILE = "MISSING_SHIPPING_PROFILE"
    MISSING_SIZE = "MISSING_SIZE"
    MISSING_TAX_CATEGORY = "MISSING_TAX_CATEGORY"
    NEGATIVE_COMMUNITY_FEEDBACK = "NEGATIVE_COMMUNITY_FEEDBACK"
    NEGATIVE_PRICE = "NEGATIVE_PRICE"
    NOT_ENOUGH_IMAGES = "NOT_ENOUGH_IMAGES"
    NOT_ENOUGH_UNIQUE_PRODUCTS = "NOT_ENOUGH_UNIQUE_PRODUCTS"
    NO_CONTENT_ID = "NO_CONTENT_ID"
    OVERLAY_DISCLAIMER_EXCEEDED_MAX_LENGTH = "OVERLAY_DISCLAIMER_EXCEEDED_MAX_LENGTH"
    PART_OF_PRODUCT_LAUNCH = "PART_OF_PRODUCT_LAUNCH"
    PASSING_MULTIPLE_CONTENT_IDS = "PASSING_MULTIPLE_CONTENT_IDS"
    PRODUCT_DOMINANT_CURRENCY_MISMATCH = "PRODUCT_DOMINANT_CURRENCY_MISMATCH"
    PRODUCT_EXPIRED = "PRODUCT_EXPIRED"
    PRODUCT_ITEM_HIDDEN_FROM_ALL_SHOPS = "PRODUCT_ITEM_HIDDEN_FROM_ALL_SHOPS"
    PRODUCT_ITEM_INVALID_PARTNER_TOKENS = "PRODUCT_ITEM_INVALID_PARTNER_TOKENS"
    PRODUCT_ITEM_NOT_INCLUDED_IN_ANY_SHOP = "PRODUCT_ITEM_NOT_INCLUDED_IN_ANY_SHOP"
    PRODUCT_ITEM_NOT_VISIBLE = "PRODUCT_ITEM_NOT_VISIBLE"
    PRODUCT_NOT_APPROVED = "PRODUCT_NOT_APPROVED"
    PRODUCT_NOT_DOMINANT_CURRENCY = "PRODUCT_NOT_DOMINANT_CURRENCY"
    PRODUCT_OUT_OF_STOCK = "PRODUCT_OUT_OF_STOCK"
    PRODUCT_URL_EQUALS_DOMAIN = "PRODUCT_URL_EQUALS_DOMAIN"
    PROPERTY_PRICE_CURRENCY_NOT_SUPPORTED = "PROPERTY_PRICE_CURRENCY_NOT_SUPPORTED"
    PROPERTY_PRICE_TOO_HIGH = "PROPERTY_PRICE_TOO_HIGH"
    PROPERTY_PRICE_TOO_LOW = "PROPERTY_PRICE_TOO_LOW"
    PROPERTY_UNIT_PRICE_CURRENCY_MISMATCH_ITEM_PRICE_CURRENCY = (
        "PROPERTY_UNIT_PRICE_CURRENCY_MISMATCH_ITEM_PRICE_CURRENCY"
    )
    PROPERTY_VALUE_CONTAINS_HTML_TAGS = "PROPERTY_VALUE_CONTAINS_HTML_TAGS"
    PROPERTY_VALUE_DESCRIPTION_CONTAINS_OFF_PLATFORM_LINK = (
        "PROPERTY_VALUE_DESCRIPTION_CONTAINS_OFF_PLATFORM_LINK"
    )
    PROPERTY_VALUE_FORMAT = "PROPERTY_VALUE_FORMAT"
    PROPERTY_VALUE_MISSING = "PROPERTY_VALUE_MISSING"
    PROPERTY_VALUE_MISSING_WARNING = "PROPERTY_VALUE_MISSING_WARNING"
    PROPERTY_VALUE_NON_POSITIVE = "PROPERTY_VALUE_NON_POSITIVE"
    PROPERTY_VALUE_STRING_EXCEEDS_LENGTH = "PROPERTY_VALUE_STRING_EXCEEDS_LENGTH"
    PROPERTY_VALUE_STRING_TOO_SHORT = "PROPERTY_VALUE_STRING_TOO_SHORT"
    PROPERTY_VALUE_UPPERCASE = "PROPERTY_VALUE_UPPERCASE"
    PROPERTY_VALUE_UPPERCASE_WARNING = "PROPERTY_VALUE_UPPERCASE_WARNING"
    PURCHASE_RATE_BELOW_ADDTOCART = "PURCHASE_RATE_BELOW_ADDTOCART"
    PURCHASE_RATE_BELOW_VIEWCONTENT = "PURCHASE_RATE_BELOW_VIEWCONTENT"
    QUALITY_DUPLICATED_DESCRIPTION = "QUALITY_DUPLICATED_DESCRIPTION"
    QUALITY_ITEM_LINK_BROKEN = "QUALITY_ITEM_LINK_BROKEN"
    QUALITY_ITEM_LINK_REDIRECTING = "QUALITY_ITEM_LINK_REDIRECTING"
    RETAILER_ID_NOT_PROVIDED = "RETAILER_ID_NOT_PROVIDED"
    SHOPIFY_INVALID_RETAILER_ID = "SHOPIFY_INVALID_RETAILER_ID"
    SHOPIFY_ITEM_MISSING_SHIPPING_PROFILE = "SHOPIFY_ITEM_MISSING_SHIPPING_PROFILE"
    SHOPS_POLICY_VIOLATION = "SHOPS_POLICY_VIOLATION"
    SUBSCRIPTION_INFO_NOT_ENABLED_FOR_FEED = "SUBSCRIPTION_INFO_NOT_ENABLED_FOR_FEED"
    TAX_CATEGORY_NOT_SUPPORTED_IN_UK = "TAX_CATEGORY_NOT_SUPPORTED_IN_UK"
    UNIQUE_PRODUCT_IDENTIFIER_MISSING = "UNIQUE_PRODUCT_IDENTIFIER_MISSING"
    UNMATCHED_EVENTS = "UNMATCHED_EVENTS"
    UNSUPPORTED_PRODUCT_CATEGORY = "UNSUPPORTED_PRODUCT_CATEGORY"
    VARIANT_ATTRIBUTE_ISSUE = "VARIANT_ATTRIBUTE_ISSUE"
    VIDEO_FETCH_FAILED = "VIDEO_FETCH_FAILED"
    VIDEO_FETCH_FAILED_BAD_GATEWAY = "VIDEO_FETCH_FAILED_BAD_GATEWAY"
    VIDEO_FETCH_FAILED_FILE_SIZE_EXCEEDED = "VIDEO_FETCH_FAILED_FILE_SIZE_EXCEEDED"
    VIDEO_FETCH_FAILED_FORBIDDEN = "VIDEO_FETCH_FAILED_FORBIDDEN"
    VIDEO_FETCH_FAILED_LINK_BROKEN = "VIDEO_FETCH_FAILED_LINK_BROKEN"
    VIDEO_FETCH_FAILED_TIMED_OUT = "VIDEO_FETCH_FAILED_TIMED_OUT"
    VIDEO_NOT_DOWNLOADABLE = "VIDEO_NOT_DOWNLOADABLE"
    WHATSAPP_DISABLED_BY_USER = "WHATSAPP_DISABLED_BY_USER"
    WHATSAPP_MARKETING_MESSAGE_DISABLED_BY_USER = "WHATSAPP_MARKETING_MESSAGE_DISABLED_BY_USER"
    WHATSAPP_MARKETING_MESSAGE_POLICY_VIOLATION = "WHATSAPP_MARKETING_MESSAGE_POLICY_VIOLATION"
    WHATSAPP_POLICY_VIOLATION = "WHATSAPP_POLICY_VIOLATION"


class productcatalogdata_sources_ingestion_source_type_enum_param(str, Enum):
    """productcatalogdata_sources_ingestion_source_type_enum_param enum values."""

    ALL = "ALL"
    PRIMARY = "PRIMARY"
    SUPPLEMENTARY = "SUPPLEMENTARY"


class productcatalogproduct_feeds_feed_type_enum_param(str, Enum):
    """productcatalogproduct_feeds_feed_type_enum_param enum values."""

    AUTOMOTIVE_MODEL = "AUTOMOTIVE_MODEL"
    COLLECTION = "COLLECTION"
    DESTINATION = "DESTINATION"
    FLIGHT = "FLIGHT"
    HOME_LISTING = "HOME_LISTING"
    HOTEL = "HOTEL"
    HOTEL_ROOM = "HOTEL_ROOM"
    LOCAL_INVENTORY = "LOCAL_INVENTORY"
    MEDIA_TITLE = "MEDIA_TITLE"
    OFFER = "OFFER"
    PRODUCTS = "PRODUCTS"
    PRODUCT_RATINGS_AND_REVIEWS = "PRODUCT_RATINGS_AND_REVIEWS"
    TRANSACTABLE_ITEMS = "TRANSACTABLE_ITEMS"
    VEHICLES = "VEHICLES"
    VEHICLE_OFFER = "VEHICLE_OFFER"


# Field literal type
ProductCatalogField = Literal[
    "ad_account_to_collaborative_ads_share_settings",
    "agency_collaborative_ads_share_settings",
    "business",
    "catalog_store",
    "commerce_merchant_settings",
    "creator_user",
    "da_display_settings",
    "default_image_url",
    "fallback_image_url",
    "feed_count",
    "id",
    "is_catalog_segment",
    "is_local_catalog",
    "name",
    "owner_business",
    "product_count",
    "store_catalog_settings",
    "user_access_expire_time",
    "vertical",
]


class ProductCatalogFields(BaseModel):
    """Pydantic model for ProductCatalog fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad_account_to_collaborative_ads_share_settings: CollaborativeAdsShareSettingsFields = Field(
        None, alias="ad_account_to_collaborative_ads_share_settings"
    )
    agency_collaborative_ads_share_settings: CollaborativeAdsShareSettingsFields = Field(
        None, alias="agency_collaborative_ads_share_settings"
    )
    business: BusinessFields = Field(None, alias="business")
    catalog_store: StoreCatalogSettingsFields = Field(None, alias="catalog_store")
    commerce_merchant_settings: CommerceMerchantSettingsFields = Field(
        None, alias="commerce_merchant_settings"
    )
    creator_user: UserFields = Field(None, alias="creator_user")
    da_display_settings: ProductCatalogImageSettingsFields = Field(
        None, alias="da_display_settings"
    )
    default_image_url: str = Field(None, alias="default_image_url")
    fallback_image_url: list[str] = Field(None, alias="fallback_image_url")
    feed_count: int = Field(None, alias="feed_count")
    id: str = Field(None, alias="id")
    is_catalog_segment: bool = Field(None, alias="is_catalog_segment")
    is_local_catalog: bool = Field(None, alias="is_local_catalog")
    name: str = Field(None, alias="name")
    owner_business: BusinessFields = Field(None, alias="owner_business")
    product_count: int = Field(None, alias="product_count")
    store_catalog_settings: StoreCatalogSettingsFields = Field(None, alias="store_catalog_settings")
    user_access_expire_time: datetime = Field(None, alias="user_access_expire_time")
    vertical: str = Field(None, alias="vertical")


class ProductCatalogDeleteAgenciesParams(BaseModel):
    """Parameters for ProductCatalog.delete_agencies()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class ProductCatalogCreateAgencieParams(BaseModel):
    """Parameters for ProductCatalog.create_agencie()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")
    permitted_roles: list[productcatalogagencies_permitted_roles_enum_param] | None = Field(
        None, description="permitted_roles parameter"
    )
    permitted_tasks: list[productcatalogagencies_permitted_tasks_enum_param] | None = Field(
        None, description="permitted_tasks parameter"
    )
    skip_defaults: bool | None = Field(None, description="skip_defaults parameter")
    utm_settings: dict[str, Any] | None = Field(None, description="utm_settings parameter")


class ProductCatalogDeleteAssignedUsersParams(BaseModel):
    """Parameters for ProductCatalog.delete_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    user: int | None = Field(None, description="user parameter")


class ProductCatalogGetAssignedUsersParams(BaseModel):
    """Parameters for ProductCatalog.get_assigned_users()."""

    model_config = ConfigDict(extra="forbid")
    business: str | None = Field(None, description="business parameter")


class ProductCatalogCreateAssignedUserParams(BaseModel):
    """Parameters for ProductCatalog.create_assigned_user()."""

    model_config = ConfigDict(extra="forbid")
    tasks: list[productcatalogassigned_users_tasks_enum_param] | None = Field(
        None, description="tasks parameter"
    )
    user: int | None = Field(None, description="user parameter")


class ProductCatalogGetAutomotiveModelsParams(BaseModel):
    """Parameters for ProductCatalog.get_automotive_models()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductCatalogCreateBatchParams(BaseModel):
    """Parameters for ProductCatalog.create_batch()."""

    model_config = ConfigDict(extra="forbid")
    allow_upsert: bool | None = Field(None, description="allow_upsert parameter")
    fbe_external_business_id: str | None = Field(
        None, description="fbe_external_business_id parameter"
    )
    requests: list[dict[str, Any]] | None = Field(None, description="requests parameter")
    version: int | None = Field(None, description="version parameter")


class ProductCatalogCreateCatalogStoreParams(BaseModel):
    """Parameters for ProductCatalog.create_catalog_store()."""

    model_config = ConfigDict(extra="forbid")
    page: str | None = Field(None, description="page parameter")


class ProductCatalogGetCategoriesParams(BaseModel):
    """Parameters for ProductCatalog.get_categories()."""

    model_config = ConfigDict(extra="forbid")
    categorization_criteria: productcatalogcategories_categorization_criteria_enum_param | None = (
        Field(None, description="categorization_criteria parameter")
    )
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductCatalogCreateCategorieParams(BaseModel):
    """Parameters for ProductCatalog.create_categorie()."""

    model_config = ConfigDict(extra="forbid")
    data: list[dict[str, Any]] | None = Field(None, description="data parameter")


class ProductCatalogGetCheckBatchRequestStatusParams(BaseModel):
    """Parameters for ProductCatalog.get_check_batch_request_status()."""

    model_config = ConfigDict(extra="forbid")
    error_priority: productcatalogcheck_batch_request_status_error_priority_enum_param | None = (
        Field(None, description="error_priority parameter")
    )
    handle: str | None = Field(None, description="handle parameter")
    load_ids_of_invalid_requests: bool | None = Field(
        None, description="load_ids_of_invalid_requests parameter"
    )


class ProductCatalogGetCheckMarketplacePartnerSellersStatusParams(BaseModel):
    """Parameters for ProductCatalog.get_check_marketplace_partner_sellers_status()."""

    model_config = ConfigDict(extra="forbid")
    session_id: str | None = Field(None, description="session_id parameter")


class ProductCatalogCreateCpasLsbImageBankParams(BaseModel):
    """Parameters for ProductCatalog.create_cpas_lsb_image_bank()."""

    model_config = ConfigDict(extra="forbid")
    ad_group_id: int | None = Field(None, description="ad_group_id parameter")
    agency_business_id: int | None = Field(None, description="agency_business_id parameter")
    backup_image_urls: list[str] | None = Field(None, description="backup_image_urls parameter")


class ProductCatalogGetCreatorAssetCreativesParams(BaseModel):
    """Parameters for ProductCatalog.get_creator_asset_creatives()."""

    model_config = ConfigDict(extra="forbid")
    moderation_status: productcatalogcreator_asset_creatives_moderation_status_enum_param | None = (
        Field(None, description="moderation_status parameter")
    )


class ProductCatalogGetDataSourcesParams(BaseModel):
    """Parameters for ProductCatalog.get_data_sources()."""

    model_config = ConfigDict(extra="forbid")
    ingestion_source_type: productcatalogdata_sources_ingestion_source_type_enum_param | None = (
        Field(None, description="ingestion_source_type parameter")
    )


class ProductCatalogGetDestinationsParams(BaseModel):
    """Parameters for ProductCatalog.get_destinations()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductCatalogGetDiagnosticsParams(BaseModel):
    """Parameters for ProductCatalog.get_diagnostics()."""

    model_config = ConfigDict(extra="forbid")
    affected_channels: list[productcatalogdiagnostics_affected_channels_enum_param] | None = Field(
        None, description="affected_channels parameter"
    )
    affected_entities: list[productcatalogdiagnostics_affected_entities_enum_param] | None = Field(
        None, description="affected_entities parameter"
    )
    affected_features: list[productcatalogdiagnostics_affected_features_enum_param] | None = Field(
        None, description="affected_features parameter"
    )
    severities: list[productcatalogdiagnostics_severities_enum_param] | None = Field(
        None, description="severities parameter"
    )
    types: list[productcatalogdiagnostics_types_enum_param] | None = Field(
        None, description="types parameter"
    )


class ProductCatalogGetEventStatsParams(BaseModel):
    """Parameters for ProductCatalog.get_event_stats()."""

    model_config = ConfigDict(extra="forbid")
    breakdowns: list[productcatalogevent_stats_breakdowns_enum_param] | None = Field(
        None, description="breakdowns parameter"
    )


class ProductCatalogDeleteExternalEventSourcesParams(BaseModel):
    """Parameters for ProductCatalog.delete_external_event_sources()."""

    model_config = ConfigDict(extra="forbid")
    external_event_sources: dict[str, Any] | None = Field(
        None, description="external_event_sources parameter"
    )


class ProductCatalogCreateExternalEventSourceParams(BaseModel):
    """Parameters for ProductCatalog.create_external_event_source()."""

    model_config = ConfigDict(extra="forbid")
    external_event_sources: dict[str, Any] | None = Field(
        None, description="external_event_sources parameter"
    )


class ProductCatalogGetFlightsParams(BaseModel):
    """Parameters for ProductCatalog.get_flights()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductCatalogCreateGeolocatedItemsBatchParams(BaseModel):
    """Parameters for ProductCatalog.create_geolocated_items_batch()."""

    model_config = ConfigDict(extra="forbid")
    allow_upsert: bool | None = Field(None, description="allow_upsert parameter")
    item_type: str | None = Field(None, description="item_type parameter")
    requests: dict[str, Any] | None = Field(None, description="requests parameter")


class ProductCatalogGetHomeListingsParams(BaseModel):
    """Parameters for ProductCatalog.get_home_listings()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductCatalogCreateHomeListingParams(BaseModel):
    """Parameters for ProductCatalog.create_home_listing()."""

    model_config = ConfigDict(extra="forbid")
    address: dict[str, Any] | None = Field(None, description="address parameter")
    availability: str | None = Field(None, description="availability parameter")
    currency: str | None = Field(None, description="currency parameter")
    description: str | None = Field(None, description="description parameter")
    home_listing_id: str | None = Field(None, description="home_listing_id parameter")
    images: list[dict[str, Any]] | None = Field(None, description="images parameter")
    listing_type: str | None = Field(None, description="listing_type parameter")
    name: str | None = Field(None, description="name parameter")
    num_baths: float | None = Field(None, description="num_baths parameter")
    num_beds: float | None = Field(None, description="num_beds parameter")
    num_units: float | None = Field(None, description="num_units parameter")
    price: float | None = Field(None, description="price parameter")
    property_type: str | None = Field(None, description="property_type parameter")
    url: str | None = Field(None, description="url parameter")
    year_built: int | None = Field(None, description="year_built parameter")


class ProductCatalogGetHotelRoomsBatchParams(BaseModel):
    """Parameters for ProductCatalog.get_hotel_rooms_batch()."""

    model_config = ConfigDict(extra="forbid")
    handle: str | None = Field(None, description="handle parameter")


class ProductCatalogCreateHotelRoomsBatchParams(BaseModel):
    """Parameters for ProductCatalog.create_hotel_rooms_batch()."""

    model_config = ConfigDict(extra="forbid")
    file: dict[str, Any] | None = Field(None, description="file parameter")
    password: str | None = Field(None, description="password parameter")
    standard: productcataloghotel_rooms_batch_standard_enum_param | None = Field(
        None, description="standard parameter"
    )
    update_only: bool | None = Field(None, description="update_only parameter")
    url: str | None = Field(None, description="url parameter")
    username: str | None = Field(None, description="username parameter")


class ProductCatalogGetHotelsParams(BaseModel):
    """Parameters for ProductCatalog.get_hotels()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductCatalogCreateHotelParams(BaseModel):
    """Parameters for ProductCatalog.create_hotel()."""

    model_config = ConfigDict(extra="forbid")
    address: dict[str, Any] | None = Field(None, description="address parameter")
    applinks: dict[str, Any] | None = Field(None, description="applinks parameter")
    base_price: int | None = Field(None, description="base_price parameter")
    brand: str | None = Field(None, description="brand parameter")
    currency: str | None = Field(None, description="currency parameter")
    description: str | None = Field(None, description="description parameter")
    guest_ratings: list[dict[str, Any]] | None = Field(None, description="guest_ratings parameter")
    hotel_id: str | None = Field(None, description="hotel_id parameter")
    images: list[dict[str, Any]] | None = Field(None, description="images parameter")
    name: str | None = Field(None, description="name parameter")
    phone: str | None = Field(None, description="phone parameter")
    star_rating: float | None = Field(None, description="star_rating parameter")
    url: str | None = Field(None, description="url parameter")


class ProductCatalogCreateItemsBatchParams(BaseModel):
    """Parameters for ProductCatalog.create_items_batch()."""

    model_config = ConfigDict(extra="forbid")
    allow_upsert: bool | None = Field(None, description="allow_upsert parameter")
    item_sub_type: productcatalogitems_batch_item_sub_type_enum_param | None = Field(
        None, description="item_sub_type parameter"
    )
    item_type: str | None = Field(None, description="item_type parameter")
    requests: dict[str, Any] | None = Field(None, description="requests parameter")
    version: int | None = Field(None, description="version parameter")


class ProductCatalogCreateLocalizedItemsBatchParams(BaseModel):
    """Parameters for ProductCatalog.create_localized_items_batch()."""

    model_config = ConfigDict(extra="forbid")
    allow_upsert: bool | None = Field(None, description="allow_upsert parameter")
    item_type: str | None = Field(None, description="item_type parameter")
    requests: dict[str, Any] | None = Field(None, description="requests parameter")
    version: int | None = Field(None, description="version parameter")


class ProductCatalogCreateMarketplacePartnerSellersDetailParams(BaseModel):
    """Parameters for ProductCatalog.create_marketplace_partner_sellers_detail()."""

    model_config = ConfigDict(extra="forbid")
    requests: dict[str, Any] | None = Field(None, description="requests parameter")


class ProductCatalogCreateMarketplacePartnerSignalParams(BaseModel):
    """Parameters for ProductCatalog.create_marketplace_partner_signal()."""

    model_config = ConfigDict(extra="forbid")
    event_name: productcatalogmarketplace_partner_signals_event_name_enum_param | None = Field(
        None, description="event_name parameter"
    )
    event_source_url: str | None = Field(None, description="event_source_url parameter")
    event_time: datetime | None = Field(None, description="event_time parameter")
    order_data: dict[str, Any] | None = Field(None, description="order_data parameter")
    user_data: dict[str, Any] | None = Field(None, description="user_data parameter")


class ProductCatalogGetPricingVariablesBatchParams(BaseModel):
    """Parameters for ProductCatalog.get_pricing_variables_batch()."""

    model_config = ConfigDict(extra="forbid")
    handle: str | None = Field(None, description="handle parameter")


class ProductCatalogCreatePricingVariablesBatchParams(BaseModel):
    """Parameters for ProductCatalog.create_pricing_variables_batch()."""

    model_config = ConfigDict(extra="forbid")
    file: dict[str, Any] | None = Field(None, description="file parameter")
    password: str | None = Field(None, description="password parameter")
    standard: productcatalogpricing_variables_batch_standard_enum_param | None = Field(
        None, description="standard parameter"
    )
    update_only: bool | None = Field(None, description="update_only parameter")
    url: str | None = Field(None, description="url parameter")
    username: str | None = Field(None, description="username parameter")


class ProductCatalogCreateProductFeedParams(BaseModel):
    """Parameters for ProductCatalog.create_product_feed()."""

    model_config = ConfigDict(extra="forbid")
    country: str | None = Field(None, description="country parameter")
    default_currency: str | None = Field(None, description="default_currency parameter")
    deletion_enabled: bool | None = Field(None, description="deletion_enabled parameter")
    delimiter: productcatalogproduct_feeds_delimiter_enum_param | None = Field(
        None, description="delimiter parameter"
    )
    encoding: productcatalogproduct_feeds_encoding_enum_param | None = Field(
        None, description="encoding parameter"
    )
    feed_type: productcatalogproduct_feeds_feed_type_enum_param | None = Field(
        None, description="feed_type parameter"
    )
    file_name: str | None = Field(None, description="file_name parameter")
    ingestion_source_type: productcatalogproduct_feeds_ingestion_source_type_enum_param | None = (
        Field(None, description="ingestion_source_type parameter")
    )
    item_sub_type: productcatalogproduct_feeds_item_sub_type_enum_param | None = Field(
        None, description="item_sub_type parameter"
    )
    migrated_from_feed_id: str | None = Field(None, description="migrated_from_feed_id parameter")
    name: str | None = Field(None, description="name parameter")
    override_type: productcatalogproduct_feeds_override_type_enum_param | None = Field(
        None, description="override_type parameter"
    )
    override_value: str | None = Field(None, description="override_value parameter")
    primary_feed_ids: list[str] | None = Field(None, description="primary_feed_ids parameter")
    quoted_fields_mode: productcatalogproduct_feeds_quoted_fields_mode_enum_param | None = Field(
        None, description="quoted_fields_mode parameter"
    )
    rules: list[str] | None = Field(None, description="rules parameter")
    schedule: str | None = Field(None, description="schedule parameter")
    selected_override_fields: list[str] | None = Field(
        None, description="selected_override_fields parameter"
    )
    update_schedule: str | None = Field(None, description="update_schedule parameter")


class ProductCatalogCreateProductGroupParams(BaseModel):
    """Parameters for ProductCatalog.create_product_group()."""

    model_config = ConfigDict(extra="forbid")
    retailer_id: str | None = Field(None, description="retailer_id parameter")
    variants: list[dict[str, Any]] | None = Field(None, description="variants parameter")


class ProductCatalogGetProductSetsParams(BaseModel):
    """Parameters for ProductCatalog.get_product_sets()."""

    model_config = ConfigDict(extra="forbid")
    ancestor_id: str | None = Field(None, description="ancestor_id parameter")
    has_children: bool | None = Field(None, description="has_children parameter")
    parent_id: str | None = Field(None, description="parent_id parameter")
    retailer_id: str | None = Field(None, description="retailer_id parameter")


class ProductCatalogCreateProductSetParams(BaseModel):
    """Parameters for ProductCatalog.create_product_set()."""

    model_config = ConfigDict(extra="forbid")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")
    metadata: dict[str, Any] | None = Field(None, description="metadata parameter")
    name: str | None = Field(None, description="name parameter")
    ordering_info: list[int] | None = Field(None, description="ordering_info parameter")
    publish_to_shops: list[dict[str, Any]] | None = Field(
        None, description="publish_to_shops parameter"
    )
    retailer_id: str | None = Field(None, description="retailer_id parameter")


class ProductCatalogGetProductSetsBatchParams(BaseModel):
    """Parameters for ProductCatalog.get_product_sets_batch()."""

    model_config = ConfigDict(extra="forbid")
    handle: str | None = Field(None, description="handle parameter")


class ProductCatalogGetProductSParams(BaseModel):
    """Parameters for ProductCatalog.get_product_s()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    error_priority: productcatalogproducts_error_priority_enum_param | None = Field(
        None, description="error_priority parameter"
    )
    error_type: productcatalogproducts_error_type_enum_param | None = Field(
        None, description="error_type parameter"
    )
    filter: dict[str, Any] | None = Field(None, description="filter parameter")
    return_only_approved_products: bool | None = Field(
        None, description="return_only_approved_products parameter"
    )


class ProductCatalogCreateProductParams(BaseModel):
    """Parameters for ProductCatalog.create_product_()."""

    model_config = ConfigDict(extra="forbid")
    additional_image_urls: list[str] | None = Field(
        None, description="additional_image_urls parameter"
    )
    additional_variant_attributes: dict[str, Any] | None = Field(
        None, description="additional_variant_attributes parameter"
    )
    age_group: productcatalogproducts_age_group_enum_param | None = Field(
        None, description="age_group parameter"
    )
    android_app_name: str | None = Field(None, description="android_app_name parameter")
    android_class: str | None = Field(None, description="android_class parameter")
    android_package: str | None = Field(None, description="android_package parameter")
    android_url: str | None = Field(None, description="android_url parameter")
    availability: productcatalogproducts_availability_enum_param | None = Field(
        None, description="availability parameter"
    )
    brand: str | None = Field(None, description="brand parameter")
    category: str | None = Field(None, description="category parameter")
    category_specific_fields: dict[str, Any] | None = Field(
        None, description="category_specific_fields parameter"
    )
    checkout_url: str | None = Field(None, description="checkout_url parameter")
    color: str | None = Field(None, description="color parameter")
    commerce_tax_category: productcatalogproducts_commerce_tax_category_enum_param | None = Field(
        None, description="commerce_tax_category parameter"
    )
    condition: productcatalogproducts_condition_enum_param | None = Field(
        None, description="condition parameter"
    )
    currency: str | None = Field(None, description="currency parameter")
    custom_data: dict[str, Any] | None = Field(None, description="custom_data parameter")
    custom_label_0: str | None = Field(None, description="custom_label_0 parameter")
    custom_label_1: str | None = Field(None, description="custom_label_1 parameter")
    custom_label_2: str | None = Field(None, description="custom_label_2 parameter")
    custom_label_3: str | None = Field(None, description="custom_label_3 parameter")
    custom_label_4: str | None = Field(None, description="custom_label_4 parameter")
    custom_number_0: int | None = Field(None, description="custom_number_0 parameter")
    custom_number_1: int | None = Field(None, description="custom_number_1 parameter")
    custom_number_2: int | None = Field(None, description="custom_number_2 parameter")
    custom_number_3: int | None = Field(None, description="custom_number_3 parameter")
    custom_number_4: int | None = Field(None, description="custom_number_4 parameter")
    description: str | None = Field(None, description="description parameter")
    expiration_date: str | None = Field(None, description="expiration_date parameter")
    fb_product_category: str | None = Field(None, description="fb_product_category parameter")
    gender: productcatalogproducts_gender_enum_param | None = Field(
        None, description="gender parameter"
    )
    gtin: str | None = Field(None, description="gtin parameter")
    image_url: str | None = Field(None, description="image_url parameter")
    importer_address: dict[str, Any] | None = Field(None, description="importer_address parameter")
    importer_name: str | None = Field(None, description="importer_name parameter")
    inventory: int | None = Field(None, description="inventory parameter")
    ios_app_name: str | None = Field(None, description="ios_app_name parameter")
    ios_app_store_id: int | None = Field(None, description="ios_app_store_id parameter")
    ios_url: str | None = Field(None, description="ios_url parameter")
    ipad_app_name: str | None = Field(None, description="ipad_app_name parameter")
    ipad_app_store_id: int | None = Field(None, description="ipad_app_store_id parameter")
    ipad_url: str | None = Field(None, description="ipad_url parameter")
    iphone_app_name: str | None = Field(None, description="iphone_app_name parameter")
    iphone_app_store_id: int | None = Field(None, description="iphone_app_store_id parameter")
    iphone_url: str | None = Field(None, description="iphone_url parameter")
    launch_date: str | None = Field(None, description="launch_date parameter")
    manufacturer_info: str | None = Field(None, description="manufacturer_info parameter")
    manufacturer_part_number: str | None = Field(
        None, description="manufacturer_part_number parameter"
    )
    marked_for_product_launch: (
        productcatalogproducts_marked_for_product_launch_enum_param | None
    ) = Field(None, description="marked_for_product_launch parameter")
    material: str | None = Field(None, description="material parameter")
    mobile_link: str | None = Field(None, description="mobile_link parameter")
    name: str | None = Field(None, description="name parameter")
    ordering_index: int | None = Field(None, description="ordering_index parameter")
    origin_country: productcatalogproducts_origin_country_enum_param | None = Field(
        None, description="origin_country parameter"
    )
    pattern: str | None = Field(None, description="pattern parameter")
    price: int | None = Field(None, description="price parameter")
    product_priority_0: float | None = Field(None, description="product_priority_0 parameter")
    product_priority_1: float | None = Field(None, description="product_priority_1 parameter")
    product_priority_2: float | None = Field(None, description="product_priority_2 parameter")
    product_priority_3: float | None = Field(None, description="product_priority_3 parameter")
    product_priority_4: float | None = Field(None, description="product_priority_4 parameter")
    product_type: str | None = Field(None, description="product_type parameter")
    quantity_to_sell_on_facebook: int | None = Field(
        None, description="quantity_to_sell_on_facebook parameter"
    )
    retailer_id: str | None = Field(None, description="retailer_id parameter")
    retailer_product_group_id: str | None = Field(
        None, description="retailer_product_group_id parameter"
    )
    return_policy_days: int | None = Field(None, description="return_policy_days parameter")
    sale_price: int | None = Field(None, description="sale_price parameter")
    sale_price_end_date: datetime | None = Field(None, description="sale_price_end_date parameter")
    sale_price_start_date: datetime | None = Field(
        None, description="sale_price_start_date parameter"
    )
    short_description: str | None = Field(None, description="short_description parameter")
    size: str | None = Field(None, description="size parameter")
    start_date: str | None = Field(None, description="start_date parameter")
    url: str | None = Field(None, description="url parameter")
    visibility: productcatalogproducts_visibility_enum_param | None = Field(
        None, description="visibility parameter"
    )
    wa_compliance_category: productcatalogproducts_wa_compliance_category_enum_param | None = Field(
        None, description="wa_compliance_category parameter"
    )
    windows_phone_app_id: str | None = Field(None, description="windows_phone_app_id parameter")
    windows_phone_app_name: str | None = Field(None, description="windows_phone_app_name parameter")
    windows_phone_url: str | None = Field(None, description="windows_phone_url parameter")


class ProductCatalogCreateUpdateGeneratedImageConfigParams(BaseModel):
    """Parameters for ProductCatalog.create_update_generated_image_config()."""

    model_config = ConfigDict(extra="forbid")
    data: list[dict[str, Any]] | None = Field(None, description="data parameter")


class ProductCatalogGetVehicleOffersParams(BaseModel):
    """Parameters for ProductCatalog.get_vehicle_offers()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductCatalogGetVehiclesParams(BaseModel):
    """Parameters for ProductCatalog.get_vehicles()."""

    model_config = ConfigDict(extra="forbid")
    bulk_pagination: bool | None = Field(None, description="bulk_pagination parameter")
    filter: dict[str, Any] | None = Field(None, description="filter parameter")


class ProductCatalogCreateVehicleParams(BaseModel):
    """Parameters for ProductCatalog.create_vehicle()."""

    model_config = ConfigDict(extra="forbid")
    address: dict[str, Any] | None = Field(None, description="address parameter")
    applinks: dict[str, Any] | None = Field(None, description="applinks parameter")
    availability: productcatalogvehicles_availability_enum_param | None = Field(
        None, description="availability parameter"
    )
    body_style: productcatalogvehicles_body_style_enum_param | None = Field(
        None, description="body_style parameter"
    )
    condition: productcatalogvehicles_condition_enum_param | None = Field(
        None, description="condition parameter"
    )
    currency: str | None = Field(None, description="currency parameter")
    date_first_on_lot: str | None = Field(None, description="date_first_on_lot parameter")
    dealer_id: str | None = Field(None, description="dealer_id parameter")
    dealer_name: str | None = Field(None, description="dealer_name parameter")
    dealer_phone: str | None = Field(None, description="dealer_phone parameter")
    description: str | None = Field(None, description="description parameter")
    drivetrain: productcatalogvehicles_drivetrain_enum_param | None = Field(
        None, description="drivetrain parameter"
    )
    exterior_color: str | None = Field(None, description="exterior_color parameter")
    fb_page_id: str | None = Field(None, description="fb_page_id parameter")
    fuel_type: productcatalogvehicles_fuel_type_enum_param | None = Field(
        None, description="fuel_type parameter"
    )
    images: list[dict[str, Any]] | None = Field(None, description="images parameter")
    interior_color: str | None = Field(None, description="interior_color parameter")
    make: str | None = Field(None, description="make parameter")
    mileage: dict[str, Any] | None = Field(None, description="mileage parameter")
    model: str | None = Field(None, description="model parameter")
    price: int | None = Field(None, description="price parameter")
    state_of_vehicle: productcatalogvehicles_state_of_vehicle_enum_param | None = Field(
        None, description="state_of_vehicle parameter"
    )
    title: str | None = Field(None, description="title parameter")
    transmission: productcatalogvehicles_transmission_enum_param | None = Field(
        None, description="transmission parameter"
    )
    trim: str | None = Field(None, description="trim parameter")
    url: str | None = Field(None, description="url parameter")
    vehicle_id: str | None = Field(None, description="vehicle_id parameter")
    vehicle_type: productcatalogvehicles_vehicle_type_enum_param | None = Field(
        None, description="vehicle_type parameter"
    )
    vin: str | None = Field(None, description="vin parameter")
    year: int | None = Field(None, description="year parameter")


class ProductCatalogCreateVersionItemsBatchParams(BaseModel):
    """Parameters for ProductCatalog.create_version_items_batch()."""

    model_config = ConfigDict(extra="forbid")
    allow_upsert: bool | None = Field(None, description="allow_upsert parameter")
    item_type: str | None = Field(None, description="item_type parameter")
    item_version: str | None = Field(None, description="item_version parameter")
    requests: dict[str, Any] | None = Field(None, description="requests parameter")
    version: int | None = Field(None, description="version parameter")
