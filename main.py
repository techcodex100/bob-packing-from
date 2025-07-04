from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from PIL import Image, ImageDraw, ImageFont

app = FastAPI()

# ✅ Load font
try:
    font = ImageFont.truetype("arial.ttf", 18)
except:
    font = ImageFont.load_default()

# 🔹 Function to draw box-wise characters
def draw_digits_in_boxes(draw, value, x_start, y_start, box_spacing=34, box_size=(30, 30), draw_box=False):
    for i, char in enumerate(str(value)):
        x = x_start + i * box_spacing
        y = y_start
        if draw_box:
            draw.rectangle([x - 2, y - 2, x + box_size[0], y + box_size[1]], outline="black", width=1)
        draw.text((x, y), char, font=font, fill="black")

# ✅ Input model
class RemittanceForm(BaseModel):
    branch_name: str
    branch_date: str
    pc_type: str
    applicant_name: str
    applicant_address: str
    contact_person: str
    mobile: str
    email: str
    iec_code: str
    tenor_days: str
    transaction_type: str
    lc_ref: str
    lc_date: str
    order_value: str
    commodity: str
    loan_currency: str
    loan_amount_figures: str
    loan_amount_words: str
    shipment_date: str
    hs_code: str
    origin_country: str
    destination_country: str
    buyer_name: str
    buyer_address: str
    account_number: str
    account_currency: str
    account_amount: str
    import_currency: str
    import_amount: str
    contract_no: str
    booking_date: str
    due_date: str
    contract_amount: str
    amount_utilized: str
    exchange_rate: str
    pc_no: str
    pc_tenor: str
    liq_currency: str
    liq_amount_figures: str
    liq_amount_words: str
    account_debit: str
    liq_reason: str
    final_date_pg1: str
    policy_no: str
    policy_date: str
    fema_date: str
    tenor_within: str = None
    doc_order: str = None
    doc_lc: str = None
    doc_extension: str = None
    doc_other1: str = None
    doc_other2: str = None

# ✅ POST endpoint
@app.post("/submit")
async def submit_form(data: RemittanceForm):
    page1 = Image.open("packing-credit-disbursal-form_page-0001.jpg")
    draw1 = ImageDraw.Draw(page1)

    draw1.text((1055, 105), data.branch_name, font=font, fill="black")
    draw1.text((990, 140), data.branch_date, font=font, fill="black")

    if data.pc_type.lower() == "pc":
        pass  # [455, 154, 475, 170] was PC black box
    elif data.pc_type.lower() == "pcfc":
        pass  # [725, 154, 745, 170] was PCFC black box

    draw1.text((290, 255), data.applicant_name, font=font, fill="black")
    draw1.text((290, 290), data.applicant_address, font=font, fill="black")
    draw1.text((290, 355), data.contact_person, font=font, fill="black")
    draw1.text((290, 385), data.mobile, font=font, fill="black")
    draw1.text((790, 385), data.email, font=font, fill="black")
    draw1.text((290, 420), data.iec_code, font=font, fill="black")
    draw1.text((280, 475), data.tenor_days, font=font, fill="black")

    if data.transaction_type.lower() == "running":
        pass  # [410, 535, 425, 555] was Running black box
    elif data.transaction_type.lower() == "order":
        pass  # [760, 540, 780, 555] was Order black box

    draw1.text((400, 575), data.lc_ref, font=font, fill="black")
    draw1.text((890, 575), data.lc_date, font=font, fill="black")
    draw1.text((400, 605), data.order_value, font=font, fill="black")
    draw1.text((890, 605), data.commodity, font=font, fill="black")
    draw1.text((290, 635), data.loan_currency, font=font, fill="black")
    draw1.text((290, 670), data.loan_amount_figures, font=font, fill="black")
    draw1.text((700, 655), data.loan_amount_words, font=font, fill="black")
    draw1.text((400, 705), data.shipment_date, font=font, fill="black")
    draw1.text((900, 705), data.hs_code, font=font, fill="black")
    draw1.text((310, 735), data.origin_country, font=font, fill="black")
    draw1.text((910, 735), data.destination_country, font=font, fill="black")
    draw1.text((290, 800), data.buyer_name, font=font, fill="black")
    draw1.text((290, 830), data.buyer_address, font=font, fill="black")

    draw_digits_in_boxes(draw1, data.account_number, 260, 980)
    draw_digits_in_boxes(draw1, data.account_currency, 760, 980)
    draw1.text((900, 980), data.account_amount, font=font, fill="black")
    draw1.text((700, 1020), data.import_currency, font=font, fill="black")
    draw1.text((900, 1020), data.import_amount, font=font, fill="black")

    draw_digits_in_boxes(draw1, data.booking_date, 950, 1120)
    draw1.text((400, 1120), data.contract_no, font=font, fill="black")

    draw_digits_in_boxes(draw1, data.due_date, 950, 1158)
    draw1.text((400, 1158), data.contract_amount, font=font, fill="black")

    draw1.text((400, 1195), data.amount_utilized, font=font, fill="black")
    draw1.text((400, 1225), data.exchange_rate, font=font, fill="black")
    draw_digits_in_boxes(draw1, data.pc_no, 285, 1285)
    draw1.text((290, 1320), data.pc_tenor + " days", font=font, fill="black")
    draw1.text((400, 1400), data.liq_currency, font=font, fill="black")
    draw1.text((400, 1430), data.liq_amount_figures, font=font, fill="black")
    draw1.text((700, 1420), data.liq_amount_words, font=font, fill="black")
    draw_digits_in_boxes(draw1, data.account_debit, 275, 1465)
    draw1.text((430, 1530), data.liq_reason, font=font, fill="black")
    draw_digits_in_boxes(draw1, data.final_date_pg1, 110, 1600, box_spacing=42, draw_box=False)

    page2 = Image.open("packing-credit-disbursal-form_page-0002.jpg")
    draw2 = ImageDraw.Draw(page2)

    draw2.text((620, 455), data.policy_no, font=font, fill="black")
    draw2.text((860, 460), data.policy_date, font=font, fill="black")
    draw_digits_in_boxes(draw2, data.fema_date, 105, 1375, box_spacing=42, draw_box=False)

    if data.tenor_within:
        draw2.text((1020, 180), data.tenor_within, font=font, fill="black")
    if data.doc_order:
        pass  # [50, 1560, 60, 1570] was Doc Order black box
    if data.doc_lc:
        pass  # [50, 1585, 60, 1595] was Doc LC black box
    if data.doc_extension:
        pass  # [50, 1615, 60, 1625] was Doc Extension black box
    if data.doc_other1:
        pass  # [50, 1645, 60, 1655] was Doc Other1 black box
    if data.doc_other2:
        pass  # [50, 1680, 60, 1690] was Doc Other2 black box

    # ✅ Save final PDF
    page1_rgb = page1.convert("RGB")
    page2_rgb = page2.convert("RGB")
    pdf_path = "filled_remittance_form.pdf"
    page1_rgb.save(pdf_path, save_all=True, append_images=[page2_rgb])

    return FileResponse(pdf_path, media_type="application/pdf", filename=pdf_path)
