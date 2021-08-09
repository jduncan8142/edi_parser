import os
import json


# REF*8M*COMPANYB*ORIGIN~
class REF:
    def __init__(self, data):
        self.ref_seg_header = {}
        self.ref_seg_header["RefIdQual"] = data[0].strip("\n\r\t ")
        self.ref_seg_header["CompanyName"] = data[1].strip("\n\r\t ")
        self.ref_seg_header["Inco"] = data[2].strip("\n\r\t ")
    
    def __repr__(self):
        return str(f"REF => {', '.join([str(a + '=' + b) for a, b in self.ref_seg_header.items()])}")
    
    def __str__(self):
        return str(f"REF => {', '.join([str(a + '=' + b) for a, b in self.ref_seg_header.items()])}")


# CUR*SN*USD~
class CUR:
    def __init__(self, data):
        self.cur_seg_header = {}
        self.cur_seg_header["CurIdQual"] = data[0].strip("\n\r\t ")
        self.cur_seg_header["Currency"] = data[1].strip("\n\r\t ")
    
    def __repr__(self):
        return str(f"CUR => {', '.join([str(a + '=' + b) for a, b in self.cur_seg_header.items()])}")
    
    def __str__(self):
        return str(f"CUR => {', '.join([str(a + '=' + b) for a, b in self.cur_seg_header.items()])}")


# transaction set header
class ST:
    def __init__(self, data):
        self.trans_set_header = {}
        self.trans_set_header["Type"] = data[0].strip("\n\r\t ")  # Transaction Set Type
        self.trans_set_header["CtrlNum"] = data[1].strip("\n\r\t ")  # Control Number

    def __repr__(self):
        return str(f"ST => {', '.join([str(a + '=' + b) for a, b in self.trans_set_header.items()])}")
    
    def __str__(self):
        return str(f"ST => {', '.join([str(a + '=' + b) for a, b in self.trans_set_header.items()])}")
    

#  beginning segment of the purchase order
class BEG:
    def __init__(self, data):
        self.beg_seg = {}
        self.beg_seg["Action"] = data[0].strip("\n\r\t ")  # PO Action (i.e. New, Update, etc)
        self.beg_seg["Type"] = data[1].strip("\n\r\t ")  # purchase order type
        self.beg_seg["PoNum"] = data[2].strip("\n\r\t ")  # purchase order number
        self.beg_seg["IssuanceDate"] = data[4].strip("\n\r\t ")  # Date of issuance
    
    def __repr__(self):
        return str(f"BEG => {', '.join([str(a + '=' + b) for a, b in self.beg_seg.items()])}")
    
    def __str__(self):
        return str(f"BEG => {', '.join([str(a + '=' + b) for a, b in self.beg_seg.items()])}")


# functional group header
class GS:
    def __init__(self, data):
        self.group_header = {}
        self.group_header["FuncCodeId"] = data[0].strip("\n\r\t ")  # GS01 - Functional Code Identifier
        self.group_header["AppSenderCode"] = data[1].strip("\n\r\t ")  # GS02 – Application Sender’s Code
        self.group_header["AppRecvCode"] = data[2].strip("\n\r\t ")  # GS03 – Application Receiver’s Code
        self.group_header["Date"] = data[3].strip("\n\r\t ")  # GS04 – Date
        self.group_header["Time"] = data[4].strip("\n\r\t ")  # GS05 – Time
        self.group_header["GrpCtrlNum"] = data[5].strip("\n\r\t ")  # GS06 – Group Control Number
        self.group_header["RespAgtCode"] = data[6].strip("\n\r\t ")  # GS07 – Responsible Agency Code
        self.group_header["VerRelIndIdCode"] = data[7].strip("\n\r\t ")  # GS08 – Version/Release/Industry Identifier Code

    def __repr__(self):
        return str(f"GS => {', '.join([str(a + '=' + b) for a, b in self.group_header.items()])}")
    
    def __str__(self):
        return str(f"GS => {', '.join([str(a + '=' + b) for a, b in self.group_header.items()])}")


# interchange control header
class ISA:
    def __init__(self, data):
        self.control_header = {}
        self.control_header["AuthInfoQual"] = data[0].strip("\n\r\t ")  # Authorization Information Qualifier
        self.control_header["AuthInfo"] = data[1].strip("\n\r\t ")  # Authorization Information
        self.control_header["SecInfoQual"] = data[2].strip("\n\r\t ")  # Security Information Qualifier
        self.control_header["SecInfo"] = data[3].strip("\n\r\t ")  # Security Information
        self.control_header["SenderIdQual"] = data[4].strip("\n\r\t ")  # Interchange ID Qualifier
        self.control_header["SendId"] = data[5].strip("\n\r\t ")  # Interchange Sender ID
        self.control_header["RecvIdQual"] = data[6].strip("\n\r\t ")  # Interchange ID Qualifier
        self.control_header["RecvId"] = data[7].strip("\n\r\t ")  # Interchange Receiver ID
        self.control_header["Date"] = data[8].strip("\n\r\t ")  # Interchange Date
        self.control_header["Time"] = data[9].strip("\n\r\t ")  # Interchange Time
        self.control_header["CtrlStdId"] = data[10].strip("\n\r\t ") # Interchange Control Standards Identifier
        self.control_header["CtrlVerNum"] = data[11].strip("\n\r\t ") # Interchange Control Version Number
        self.control_header["CtrlNum"] = data[12].strip("\n\r\t ") # Interchange Control Number
        self.control_header["AckReq"] = data[13].strip("\n\r\t ") # Acknowledgement Requested
        self.control_header["UseId"] = data[14].strip("\n\r\t ") # Usage Indicator
        self.control_header["CompElemSep"] = data[15].strip("\n\r\t ") # Component Element Separator
    
    def __repr__(self):
        return f"ISA => {', '.join([str(a + '=' + b) for a, b in self.control_header.items()])}"
    
    def __str__(self):
        return f"ISA => {', '.join([str(a + '=' + b) for a, b in self.control_header.items()])}"


class DataSegment():
    def __init__(self, seg_data, seg_id, seg_type=None, seg_sep=None, seg_term=None):
        self.data = seg_data
        self.id = seg_id
        self.type = seg_type
        self.sep = seg_sep if seg_sep is not None else "*"
        self.term = seg_term if seg_term is not None else "~"
        self.elements = {}
        self.parse_segment()
    
    def __repr__(self):
        return str(f"< DataSegment object <=> {''.join(str(self.elements.get(self.type)))} >")
    
    def __str__(self):
        return str(f"< DataSegment object <=> {''.join(str(self.elements.get(self.type)))} >")


    def parse_segment(self):
        _data = self.data.strip(self.term)
        _data = _data.split(self.sep)
        self.type = _data[0]
        if self.type == "ISA":
            self.elements[self.type] = ISA(_data[1:])
        elif self.type == "GS":
            self.elements[self.type] = GS(_data[1:])
        elif self.type == "ST":
            self.elements[self.type] = ST(_data[1:])
        elif self.type == "BEG":
            self.elements[self.type] = BEG(_data[1:])
        elif self.type == "CUR":
            self.elements[self.type] = CUR(_data[1:])
        elif self.type == "REF":
            self.elements[self.type] = REF(_data[1:])
        else:
            for index, element in enumerate(_data[1:]):
                self.elements[index] = str(element)


class X2Json:
    def __init__(self, filename=None, seg_term=None, seg_sep=None, element_term=None):
        self.filename = filename if filename is not None else ""
        self.raw_data = None
        self.err_msg = None
        self.data_segments = {}
        self.seg_term = seg_term if seg_term is not None else "~"
        self.seg_sep = seg_sep if seg_sep is not None else "*"

        self.read_raw_file()
        self.parse_raw()

    def read_raw_file(self):
        try:
            with open(self.filename, "r") as f:
                self.raw_data = f.readlines()
                self.err_msg = None
        except Exception as e:
            self.err_msg = e
    
    def parse_raw(self, strip_value="\n\r\t "):
        if not self.err_msg:
            for index, line in enumerate(self.raw_data):
                _line = line.strip(strip_value)
                self.data_segments[index] = DataSegment(seg_data=_line, seg_id=index, seg_sep=self.seg_sep, seg_term=self.seg_term)
        else:
            print(self.err_msg)


if __name__ == "__main__":
    x = X2Json(filename="C:/Users/duncan/OneDrive - MULTIVAC Sepp Haggenmüller SE & Co. KG/Documents/Python/edi_parser/edi_samples/850/sample1")
    [print(f"{k} >> {v.type} >> {v}") for k, v in x.data_segments.items()]