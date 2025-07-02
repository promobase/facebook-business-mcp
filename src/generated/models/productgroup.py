"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from .productcatalog import ProductCatalogFields
    from .productvariant import ProductVariantFields


class productgroupproducts_gender_enum_param(str, Enum):
    """productgroupproducts_gender_enum_param enum values."""

    female = "female"
    male = "male"
    unisex = "unisex"


class productgroupproducts_condition_enum_param(str, Enum):
    """productgroupproducts_condition_enum_param enum values."""

    cpo = "cpo"
    new = "new"
    open_box_new = "open_box_new"
    refurbished = "refurbished"
    used = "used"
    used_fair = "used_fair"
    used_good = "used_good"
    used_like_new = "used_like_new"


class productgroupproducts_visibility_enum_param(str, Enum):
    """productgroupproducts_visibility_enum_param enum values."""

    published = "published"
    staging = "staging"


class productgroupproducts_availability_enum_param(str, Enum):
    """productgroupproducts_availability_enum_param enum values."""

    AVAILABLE_FOR_ORDER = "available for order"
    discontinued = "discontinued"
    IN_STOCK = "in stock"
    mark_as_sold = "mark_as_sold"
    OUT_OF_STOCK = "out of stock"
    pending = "pending"
    preorder = "preorder"


class productgroupproducts_age_group_enum_param(str, Enum):
    """productgroupproducts_age_group_enum_param enum values."""

    adult = "adult"
    ALL_AGES = "all ages"
    infant = "infant"
    kids = "kids"
    newborn = "newborn"
    teen = "teen"
    toddler = "toddler"


class productgroupproducts_marked_for_product_launch_enum_param(str, Enum):
    """productgroupproducts_marked_for_product_launch_enum_param enum values."""

    default = "default"
    marked = "marked"
    not_marked = "not_marked"


class productgroupproducts_commerce_tax_category_enum_param(str, Enum):
    """productgroupproducts_commerce_tax_category_enum_param enum values."""

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


# Field literal type
ProductGroupField = Literal["id", "product_catalog", "retailer_id", "variants"]


class ProductGroupFields(BaseModel):
    """Pydantic model for ProductGroup fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    id: str = Field(None, alias="id")
    product_catalog: ProductCatalogFields = Field(None, alias="product_catalog")
    retailer_id: str = Field(None, alias="retailer_id")
    variants: list[ProductVariantFields] = Field(None, alias="variants")


class ProductGroupCreateProductParams(BaseModel):
    """Parameters for ProductGroup.create_product_()."""

    model_config = ConfigDict(extra="forbid")
    additional_image_urls: list[str] | None = Field(
        None, description="additional_image_urls parameter"
    )
    additional_variant_attributes: dict[str, Any] | None = Field(
        None, description="additional_variant_attributes parameter"
    )
    age_group: productgroupproducts_age_group_enum_param | None = Field(
        None, description="age_group parameter"
    )
    android_app_name: str | None = Field(None, description="android_app_name parameter")
    android_class: str | None = Field(None, description="android_class parameter")
    android_package: str | None = Field(None, description="android_package parameter")
    android_url: str | None = Field(None, description="android_url parameter")
    availability: productgroupproducts_availability_enum_param | None = Field(
        None, description="availability parameter"
    )
    brand: str | None = Field(None, description="brand parameter")
    category: str | None = Field(None, description="category parameter")
    checkout_url: str | None = Field(None, description="checkout_url parameter")
    color: str | None = Field(None, description="color parameter")
    commerce_tax_category: productgroupproducts_commerce_tax_category_enum_param | None = Field(
        None, description="commerce_tax_category parameter"
    )
    condition: productgroupproducts_condition_enum_param | None = Field(
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
    gender: productgroupproducts_gender_enum_param | None = Field(
        None, description="gender parameter"
    )
    gtin: str | None = Field(None, description="gtin parameter")
    image_url: str | None = Field(None, description="image_url parameter")
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
    manufacturer_part_number: str | None = Field(
        None, description="manufacturer_part_number parameter"
    )
    marked_for_product_launch: productgroupproducts_marked_for_product_launch_enum_param | None = (
        Field(None, description="marked_for_product_launch parameter")
    )
    material: str | None = Field(None, description="material parameter")
    mobile_link: str | None = Field(None, description="mobile_link parameter")
    name: str | None = Field(None, description="name parameter")
    ordering_index: int | None = Field(None, description="ordering_index parameter")
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
    visibility: productgroupproducts_visibility_enum_param | None = Field(
        None, description="visibility parameter"
    )
    windows_phone_app_id: str | None = Field(None, description="windows_phone_app_id parameter")
    windows_phone_app_name: str | None = Field(None, description="windows_phone_app_name parameter")
    windows_phone_url: str | None = Field(None, description="windows_phone_url parameter")
