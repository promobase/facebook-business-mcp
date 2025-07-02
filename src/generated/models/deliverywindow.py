"""Code generated from Facebook API specs - DO NOT EDIT MANUALLY."""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel, ConfigDict, Field

# Field literal type
DeliveryWindowField = Literal[
    "ad",
    "ae",
    "af",
    "ag",
    "ai",
    "al",
    "all",
    "am",
    "an",
    "ao",
    "aq",
    "ar",
    "as",
    "at",
    "au",
    "aw",
    "ax",
    "az",
    "ba",
    "bb",
    "bd",
    "be",
    "bf",
    "bg",
    "bh",
    "bi",
    "bj",
    "bl",
    "bm",
    "bn",
    "bo",
    "bq",
    "br",
    "bs",
    "bt",
    "bv",
    "bw",
    "by",
    "bz",
    "ca",
    "cc",
    "cd",
    "cf",
    "cg",
    "ch",
    "ci",
    "ck",
    "cl",
    "cm",
    "cn",
    "co",
    "cr",
    "cu",
    "cv",
    "cw",
    "cx",
    "cy",
    "cz",
    "de",
    "dj",
    "dk",
    "dm",
    "do",
    "dz",
    "ec",
    "ee",
    "eg",
    "eh",
    "er",
    "es",
    "et",
    "fi",
    "fj",
    "fk",
    "fm",
    "fo",
    "fr",
    "ga",
    "gb",
    "gd",
    "ge",
    "gf",
    "gg",
    "gh",
    "gi",
    "gl",
    "gm",
    "gn",
    "gp",
    "gq",
    "gr",
    "gs",
    "gt",
    "gu",
    "gw",
    "gy",
    "hk",
    "hm",
    "hn",
    "hr",
    "ht",
    "hu",
    "id",
    "ie",
    "il",
    "im",
    "in",
    "io",
    "iq",
    "ir",
    "is",
    "it",
    "je",
    "jm",
    "jo",
    "jp",
    "ke",
    "kg",
    "kh",
    "ki",
    "km",
    "kn",
    "kp",
    "kr",
    "kw",
    "ky",
    "kz",
    "la",
    "lb",
    "lc",
    "li",
    "lk",
    "lr",
    "ls",
    "lt",
    "lu",
    "lv",
    "ly",
    "ma",
    "mc",
    "md",
    "me",
    "mf",
    "mg",
    "mh",
    "mk",
    "ml",
    "mm",
    "mn",
    "mo",
    "mp",
    "mq",
    "mr",
    "ms",
    "mt",
    "mu",
    "mv",
    "mw",
    "mx",
    "my",
    "mz",
    "na",
    "nc",
    "ne",
    "nf",
    "ng",
    "ni",
    "nl",
    "no",
    "np",
    "nr",
    "nu",
    "nz",
    "om",
    "pa",
    "pe",
    "pf",
    "pg",
    "ph",
    "pk",
    "pl",
    "pm",
    "pn",
    "pr",
    "ps",
    "pt",
    "pw",
    "py",
    "qa",
    "re",
    "ro",
    "rs",
    "ru",
    "rw",
    "sa",
    "sb",
    "sc",
    "sd",
    "se",
    "sg",
    "sh",
    "si",
    "sj",
    "sk",
    "sl",
    "sm",
    "sn",
    "so",
    "sr",
    "ss",
    "st",
    "sv",
    "sx",
    "sy",
    "sz",
    "tc",
    "td",
    "tf",
    "tg",
    "th",
    "tj",
    "tk",
    "tl",
    "tm",
    "tn",
    "to",
    "tr",
    "tt",
    "tv",
    "tw",
    "tz",
    "ua",
    "ug",
    "um",
    "us",
    "uy",
    "uz",
    "va",
    "vc",
    "ve",
    "vg",
    "vi",
    "vn",
    "vu",
    "wf",
    "ws",
    "xk",
    "ye",
    "yt",
    "za",
    "zm",
    "zw",
]


class DeliveryWindowFields(BaseModel):
    """Pydantic model for DeliveryWindow fields."""

    model_config = ConfigDict(populate_by_alias=True, extra="forbid")

    ad: int = Field(None, alias="ad")
    ae: int = Field(None, alias="ae")
    af: int = Field(None, alias="af")
    ag: int = Field(None, alias="ag")
    ai: int = Field(None, alias="ai")
    al: int = Field(None, alias="al")
    all: int = Field(None, alias="all")
    am: int = Field(None, alias="am")
    an: int = Field(None, alias="an")
    ao: int = Field(None, alias="ao")
    aq: int = Field(None, alias="aq")
    ar: int = Field(None, alias="ar")
    as_: int = Field(None, alias="as")
    at: int = Field(None, alias="at")
    au: int = Field(None, alias="au")
    aw: int = Field(None, alias="aw")
    ax: int = Field(None, alias="ax")
    az: int = Field(None, alias="az")
    ba: int = Field(None, alias="ba")
    bb: int = Field(None, alias="bb")
    bd: int = Field(None, alias="bd")
    be: int = Field(None, alias="be")
    bf: int = Field(None, alias="bf")
    bg: int = Field(None, alias="bg")
    bh: int = Field(None, alias="bh")
    bi: int = Field(None, alias="bi")
    bj: int = Field(None, alias="bj")
    bl: int = Field(None, alias="bl")
    bm: int = Field(None, alias="bm")
    bn: int = Field(None, alias="bn")
    bo: int = Field(None, alias="bo")
    bq: int = Field(None, alias="bq")
    br: int = Field(None, alias="br")
    bs: int = Field(None, alias="bs")
    bt: int = Field(None, alias="bt")
    bv: int = Field(None, alias="bv")
    bw: int = Field(None, alias="bw")
    by: int = Field(None, alias="by")
    bz: int = Field(None, alias="bz")
    ca: int = Field(None, alias="ca")
    cc: int = Field(None, alias="cc")
    cd: int = Field(None, alias="cd")
    cf: int = Field(None, alias="cf")
    cg: int = Field(None, alias="cg")
    ch: int = Field(None, alias="ch")
    ci: int = Field(None, alias="ci")
    ck: int = Field(None, alias="ck")
    cl: int = Field(None, alias="cl")
    cm: int = Field(None, alias="cm")
    cn: int = Field(None, alias="cn")
    co: int = Field(None, alias="co")
    cr: int = Field(None, alias="cr")
    cu: int = Field(None, alias="cu")
    cv: int = Field(None, alias="cv")
    cw: int = Field(None, alias="cw")
    cx: int = Field(None, alias="cx")
    cy: int = Field(None, alias="cy")
    cz: int = Field(None, alias="cz")
    de: int = Field(None, alias="de")
    dj: int = Field(None, alias="dj")
    dk: int = Field(None, alias="dk")
    dm: int = Field(None, alias="dm")
    do: int = Field(None, alias="do")
    dz: int = Field(None, alias="dz")
    ec: int = Field(None, alias="ec")
    ee: int = Field(None, alias="ee")
    eg: int = Field(None, alias="eg")
    eh: int = Field(None, alias="eh")
    er: int = Field(None, alias="er")
    es: int = Field(None, alias="es")
    et: int = Field(None, alias="et")
    fi: int = Field(None, alias="fi")
    fj: int = Field(None, alias="fj")
    fk: int = Field(None, alias="fk")
    fm: int = Field(None, alias="fm")
    fo: int = Field(None, alias="fo")
    fr: int = Field(None, alias="fr")
    ga: int = Field(None, alias="ga")
    gb: int = Field(None, alias="gb")
    gd: int = Field(None, alias="gd")
    ge: int = Field(None, alias="ge")
    gf: int = Field(None, alias="gf")
    gg: int = Field(None, alias="gg")
    gh: int = Field(None, alias="gh")
    gi: int = Field(None, alias="gi")
    gl: int = Field(None, alias="gl")
    gm: int = Field(None, alias="gm")
    gn: int = Field(None, alias="gn")
    gp: int = Field(None, alias="gp")
    gq: int = Field(None, alias="gq")
    gr: int = Field(None, alias="gr")
    gs: int = Field(None, alias="gs")
    gt: int = Field(None, alias="gt")
    gu: int = Field(None, alias="gu")
    gw: int = Field(None, alias="gw")
    gy: int = Field(None, alias="gy")
    hk: int = Field(None, alias="hk")
    hm: int = Field(None, alias="hm")
    hn: int = Field(None, alias="hn")
    hr: int = Field(None, alias="hr")
    ht: int = Field(None, alias="ht")
    hu: int = Field(None, alias="hu")
    id: int = Field(None, alias="id")
    ie: int = Field(None, alias="ie")
    il: int = Field(None, alias="il")
    im: int = Field(None, alias="im")
    in_: int = Field(None, alias="in")
    io: int = Field(None, alias="io")
    iq: int = Field(None, alias="iq")
    ir: int = Field(None, alias="ir")
    is_: int = Field(None, alias="is")
    it: int = Field(None, alias="it")
    je: int = Field(None, alias="je")
    jm: int = Field(None, alias="jm")
    jo: int = Field(None, alias="jo")
    jp: int = Field(None, alias="jp")
    ke: int = Field(None, alias="ke")
    kg: int = Field(None, alias="kg")
    kh: int = Field(None, alias="kh")
    ki: int = Field(None, alias="ki")
    km: int = Field(None, alias="km")
    kn: int = Field(None, alias="kn")
    kp: int = Field(None, alias="kp")
    kr: int = Field(None, alias="kr")
    kw: int = Field(None, alias="kw")
    ky: int = Field(None, alias="ky")
    kz: int = Field(None, alias="kz")
    la: int = Field(None, alias="la")
    lb: int = Field(None, alias="lb")
    lc: int = Field(None, alias="lc")
    li: int = Field(None, alias="li")
    lk: int = Field(None, alias="lk")
    lr: int = Field(None, alias="lr")
    ls: int = Field(None, alias="ls")
    lt: int = Field(None, alias="lt")
    lu: int = Field(None, alias="lu")
    lv: int = Field(None, alias="lv")
    ly: int = Field(None, alias="ly")
    ma: int = Field(None, alias="ma")
    mc: int = Field(None, alias="mc")
    md: int = Field(None, alias="md")
    me: int = Field(None, alias="me")
    mf: int = Field(None, alias="mf")
    mg: int = Field(None, alias="mg")
    mh: int = Field(None, alias="mh")
    mk: int = Field(None, alias="mk")
    ml: int = Field(None, alias="ml")
    mm: int = Field(None, alias="mm")
    mn: int = Field(None, alias="mn")
    mo: int = Field(None, alias="mo")
    mp: int = Field(None, alias="mp")
    mq: int = Field(None, alias="mq")
    mr: int = Field(None, alias="mr")
    ms: int = Field(None, alias="ms")
    mt: int = Field(None, alias="mt")
    mu: int = Field(None, alias="mu")
    mv: int = Field(None, alias="mv")
    mw: int = Field(None, alias="mw")
    mx: int = Field(None, alias="mx")
    my: int = Field(None, alias="my")
    mz: int = Field(None, alias="mz")
    na: int = Field(None, alias="na")
    nc: int = Field(None, alias="nc")
    ne: int = Field(None, alias="ne")
    nf: int = Field(None, alias="nf")
    ng: int = Field(None, alias="ng")
    ni: int = Field(None, alias="ni")
    nl: int = Field(None, alias="nl")
    no: int = Field(None, alias="no")
    np: int = Field(None, alias="np")
    nr: int = Field(None, alias="nr")
    nu: int = Field(None, alias="nu")
    nz: int = Field(None, alias="nz")
    om: int = Field(None, alias="om")
    pa: int = Field(None, alias="pa")
    pe: int = Field(None, alias="pe")
    pf: int = Field(None, alias="pf")
    pg: int = Field(None, alias="pg")
    ph: int = Field(None, alias="ph")
    pk: int = Field(None, alias="pk")
    pl: int = Field(None, alias="pl")
    pm: int = Field(None, alias="pm")
    pn: int = Field(None, alias="pn")
    pr: int = Field(None, alias="pr")
    ps: int = Field(None, alias="ps")
    pt: int = Field(None, alias="pt")
    pw: int = Field(None, alias="pw")
    py: int = Field(None, alias="py")
    qa: int = Field(None, alias="qa")
    re: int = Field(None, alias="re")
    ro: int = Field(None, alias="ro")
    rs: int = Field(None, alias="rs")
    ru: int = Field(None, alias="ru")
    rw: int = Field(None, alias="rw")
    sa: int = Field(None, alias="sa")
    sb: int = Field(None, alias="sb")
    sc: int = Field(None, alias="sc")
    sd: int = Field(None, alias="sd")
    se: int = Field(None, alias="se")
    sg: int = Field(None, alias="sg")
    sh: int = Field(None, alias="sh")
    si: int = Field(None, alias="si")
    sj: int = Field(None, alias="sj")
    sk: int = Field(None, alias="sk")
    sl: int = Field(None, alias="sl")
    sm: int = Field(None, alias="sm")
    sn: int = Field(None, alias="sn")
    so: int = Field(None, alias="so")
    sr: int = Field(None, alias="sr")
    ss: int = Field(None, alias="ss")
    st: int = Field(None, alias="st")
    sv: int = Field(None, alias="sv")
    sx: int = Field(None, alias="sx")
    sy: int = Field(None, alias="sy")
    sz: int = Field(None, alias="sz")
    tc: int = Field(None, alias="tc")
    td: int = Field(None, alias="td")
    tf: int = Field(None, alias="tf")
    tg: int = Field(None, alias="tg")
    th: int = Field(None, alias="th")
    tj: int = Field(None, alias="tj")
    tk: int = Field(None, alias="tk")
    tl: int = Field(None, alias="tl")
    tm: int = Field(None, alias="tm")
    tn: int = Field(None, alias="tn")
    to: int = Field(None, alias="to")
    tr: int = Field(None, alias="tr")
    tt: int = Field(None, alias="tt")
    tv: int = Field(None, alias="tv")
    tw: int = Field(None, alias="tw")
    tz: int = Field(None, alias="tz")
    ua: int = Field(None, alias="ua")
    ug: int = Field(None, alias="ug")
    um: int = Field(None, alias="um")
    us: int = Field(None, alias="us")
    uy: int = Field(None, alias="uy")
    uz: int = Field(None, alias="uz")
    va: int = Field(None, alias="va")
    vc: int = Field(None, alias="vc")
    ve: int = Field(None, alias="ve")
    vg: int = Field(None, alias="vg")
    vi: int = Field(None, alias="vi")
    vn: int = Field(None, alias="vn")
    vu: int = Field(None, alias="vu")
    wf: int = Field(None, alias="wf")
    ws: int = Field(None, alias="ws")
    xk: int = Field(None, alias="xk")
    ye: int = Field(None, alias="ye")
    yt: int = Field(None, alias="yt")
    za: int = Field(None, alias="za")
    zm: int = Field(None, alias="zm")
    zw: int = Field(None, alias="zw")
